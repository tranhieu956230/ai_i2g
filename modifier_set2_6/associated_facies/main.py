from csv import DictWriter, DictReader, reader
from copy import deepcopy
from utilites import utils_func

NAMES = [
    "Alluvial_Fan",
    "Fluvial_Channel",
    "Fluvial_Point_Bar",
    "Levee",
    "Crevasse_Splay",
    "Fluvial_Floodplain",
    "Progradational_Lacustrine_Delta",
    "Lacustrine_Fan_Delta",
    "Progradational_Lacustrine_Shoreface",
    "Transgressive_Lacustrine_Shoreface",
    "Aggradational_Lacustrine_Shoreface",
    "Lacustrine_Offshore_Transition",
    "Lacustrine_Shelf",
    "Proximal_Sub-Lacustrine_Fan",
    "Distal_Sub-Lacustrine_Fan",
    "Lacustrine_Turbidite",
    "Distal_Lacustrine_Turbidites",
    "Lacustrine_Deepwater",
    "Marine_Delta",
    "Marine_Fan_Delta",
    "Tidal_Channel_And_Sand_Flat",
    "Sandy_Tidal_Flat",
    "Mixed_Tidal_Flat",
    "Muddy_Tidal_Flat",
    "Lagoon",
    "Progradational_Marine_Shoreface",
    "Transgressive_Marine_Shoreface",
    "Aggradational_Marine_Shoreface",
    "Marine_Offshore_Transition",
    "Marine_Shelf",
    "Proximal_Submarine_Fan",
    "Distal_Submarine_Fan",
    "Marine_Turbidite",
    "Distal_Marine_Turbidites",
    "Marine_Deepwater"
]

GROUPS = [
    "Fluvial",
    "Shallow_Lacustrine",
    "Deep_Lacustrine",
    "Marginal_Marine",
    "Shallow_Marine",
    "Deep_Marine"
]


def find_max_curve(row):
    max = 0
    lst = []
    for name in NAMES:
        if int(row[name]) > max:
            max = int(row[name])

    if max > 0:
        for name in NAMES:
            if int(row[name]) == max:
                lst.append({name: max})
    return lst


def simplify_data(data):
    lst = []
    lithos = []

    for i in range(len(data) - 1):
        if data[i]["Special_lithology"] != "-999":
            lithos.append(int(data[i]["Special_lithology"]))
        if data[i]["Unit_index"] != data[i + 1]["Unit_index"] or i == len(data) - 1:
            final_lithologies = deepcopy(utils_func.remove_duplicate(lithos))
            data[i].update({"Special_lithologies": True if len(final_lithologies) > 0 else False, "Special_lithology": final_lithologies})
            lst.append(data[i])
            lithos.clear()

    return lst


def find_max_radius_30(unit_index, data):
    unit_index = int(unit_index)
    lst = []

    if data[unit_index]["Special_lithologies"]:
        return lst

    for i in range(unit_index, -1, -1):
        if abs(float(data[i]["TVD"]) - float(data[unit_index]["TVD"])) <= 30 and not data[i]["Special_lithologies"]:
            lst.extend(find_max_curve(data[i]))
        else:
            break

    for i in range(unit_index + 1, len(data), 1):
        if abs(float(data[i]["TVD"]) - float(data[unit_index]["TVD"])) <= 30 and not data[i]["Special_lithologies"]:
            lst.extend(find_max_curve(data[i]))
        else:
            break

    return lst


def divide_group(data):
    lst = []
    lst.append({"name": "Fluvial", "occurrence": 0, "points": 0})
    lst.append({"name": "Marginal_Marine", "occurrence": 0, "points": 0})
    lst.append({"name": "Shallow_Marine", "occurrence": 0, "points": 0})
    lst.append({"name": "Deep_Marine", "occurrence": 0, "points": 0})
    lst.append({"name": "Shallow_Lacustrine", "occurrence": 0, "points": 0})
    lst.append({"name": "Deep_Lacustrine", "occurrence": 0, "points": 0})

    for item in data:
        for key in item.keys():
            facy_name = key
        group_name = utils_func.get_group_name(facy_name)
        for l in lst:
            if l["name"] == group_name:
                l["occurrence"] += 1
                l["points"] += int(item[facy_name])

    return lst


def pick_group(data):
    idx = 0
    for i in range(len(data)):
        if int(data[i - idx]["occurrence"]) == 0:
            data.pop(i - idx)
            idx += 1
    if len(data) == 0:
        return data

    lst = sorted(data, key=lambda k: (k["occurrence"], k["points"]), reverse=True)
    first = lst[0]["points"]
    
    for item in lst:
        if item["points"] != first:
            return []

    return lst


def update_most_abundant(row, group):
    points = []
    if group["name"] == "Fluvial":
        points = [2, 0, -1, 0, -1, -2]

    if group["name"] == "Shadow_Lacustrine":
        points = [0, 2, 0, -1, -1, -2]

    if group["name"] == "Deep_Lacustrine":
        points = [-1, 0, 2, -2, -2, -2]

    if group["name"] == "Marginal_Marine":
        points = [0, -1, -2, 2, 0, -1]

    if group["name"] == "Shallow_Marine":
        points = [-1, -1, -2, 0, 2, 0]

    if group["name"] == "Deep_Marine":
        points = [-2, -1, -2, -1, 0, 2]

    for i in range(len(points)):
        row.update(utils_func.update_row_group(GROUPS[i], row, points[i]))

    return row


def update_second_most_abundant(row, group):
    points = []
    if group["name"] == "Fluvial":
        points = [1, 0, 0, 0, 0, -2]

    if group["name"] == "Shadow_Lacustrine":
        points = [0, 1, 0, 0, -1, -2]

    if group["name"] == "Deep_Lacustrine":
        points = [0, 0, 1, 1, -2, -2]

    if group["name"] == "Marginal_Marine":
        points = [0, 0, 1, 1, 0, -1]

    if group["name"] == "Shallow_Marine":
        points = [0, -1, -2, 0, 1, 0]

    if group["name"] == "Deep_Marine":
        points = [-2, -2, -2, -1, 0, 1]

    for i in range(len(points)):
        row.update(utils_func.update_row_group(GROUPS[i], row, points[i]))

    return row


def update_third_most_abundant(row, group):
    points = []
    if group["name"] == "Fluvial":
        points = [0, 0, 0, 0, 0, -1]

    if group["name"] == "Shadow_Lacustrine":
        points = [0, 0, 1, 0, 0, -1]

    if group["name"] == "Deep_Lacustrine":
        points = [0, 1, 0, 0, 0, -1]

    if group["name"] == "Marginal_Marine":
        points = [0, 0, 0, 0, 0, 0]

    if group["name"] == "Shallow_Marine":
        points = [0, 0, 0, 0, 0, 0]

    if group["name"] == "Deep_Marine":
        points = [-1, -1, -1, 0, 0, 0]

    for i in range(len(points)):
        row.update(utils_func.update_row_group(GROUPS[i], row, points[i]))

    return row


def update_4_6_most_abundant(row, group):
    points = []
    if group["name"] == "Fluvial":
        points = [-2, 0, 0, 0, 0, 0]

    if group["name"] == "Shadow_Lacustrine":
        points = [0, -2, 0, 0, 0, 0]

    if group["name"] == "Deep_Lacustrine":
        points = [0, 0, -2, 0, 0, 0]

    if group["name"] == "Marginal_Marine":
        points = [0, 0, 0, -2, 0, 0]

    if group["name"] == "Shallow_Marine":
        points = [0, 0, 0, 0, -2, 0]

    if group["name"] == "Deep_Marine":
        points = [0, 0, 0, 0, 0, -2]

    for i in range(len(points)):
        row.update(utils_func.update_row_group(GROUPS[i], row, points[i]))

    return row


def update_row(row, groups):
    if len(groups) > 0:
        row.update(update_most_abundant(row, groups[0]))

    if len(groups) > 1:
        row.update(update_second_most_abundant(row, groups[1]))

    if len(groups) > 2:
        row.update(update_third_most_abundant(row, groups[2]))

    if len(groups) > 3:
        for i in range(3, len(groups)):
            row.update(update_4_6_most_abundant(row, groups[i]))

    return row


with open("../../modifier_set1_5/stacking_pattern/stacking_pattern.csv") as file:
    reader = reader(file)
    headers = list(reader)[0]


with open("../../modifier_set1_5/stacking_pattern/stacking_pattern.csv") as i_file:
    dict_reader = DictReader(i_file)
    data = list(dict_reader)
    simplified_data = simplify_data(data)
    for i in range(0, 2):
        for row in reversed(simplified_data):
            groups = pick_group(divide_group(find_max_radius_30(row["Unit_index"], simplified_data)))
            row.update(update_row(row, groups))


with open("associated_facies.csv", "w") as o_file:
    dict_writer = DictWriter(o_file, fieldnames=headers)
    dict_writer.writeheader()
    for row in simplified_data:
        row.pop('Special_lithologies', None)
        dict_writer.writerow(row)
