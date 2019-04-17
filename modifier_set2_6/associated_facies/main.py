from csv import DictReader, reader
from copy import deepcopy
from utilites import utils_func
from modifier_set2_6.lower_boundary import lower_boundary
from modifier_set2_6.upper_boundary import upper_boundary

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

    for i in range(len(data)):
        if data[i]["Special_lithology"] != "-9999":
            lithos.append(int(data[i]["Special_lithology"]))
        if data[i]["Boundary_flag"] == "1":
            final_lithologies = deepcopy(utils_func.remove_duplicate(lithos))
            data[i].update({"Special_lithology": final_lithologies})
            lst.append(data[i])
            lithos.clear()

    return lst


def contain_special_lithology(litho):
    if litho == "[]" or not litho:
        return False
    return True


def find_max_radius_30(unit_index, data):
    unit_index = int(unit_index)
    lst = []

    if contain_special_lithology(data[unit_index]["Special_lithology"]):
        return lst

    for i in range(unit_index, -1, -1):
        if abs(float(data[i]["TVD"]) - float(data[unit_index]["TVD"])) <= 30 and not contain_special_lithology(
                data[unit_index]["Special_lithology"]):
            lst.extend(find_max_curve(data[i]))
        else:
            break

    for i in range(unit_index + 1, len(data), 1):
        if abs(float(data[i]["TVD"]) - float(data[unit_index]["TVD"])) <= 30 and not contain_special_lithology(
                data[unit_index]["Special_lithology"]):
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

    return lst


def update_most_abundant(row, group):
    points = []
    if group["name"] == "Fluvial":
        points = [2, 0, -1, 0, -1, -2]

    if group["name"] == "Shallow_Lacustrine":
        points = [0, 2, 0, -1, -1, -2]

    if group["name"] == "Deep_Lacustrine":
        points = [-1, 0, 2, -2, -2, -2]

    if group["name"] == "Marginal_Marine":
        points = [0, -1, -2, 2, 0, -1]

    if group["name"] == "Shallow_Marine":
        points = [-1, -1, -2, 0, 2, 0]

    if group["name"] == "Deep_Marine":
        points = [-2, -1, -2, -1, 0, 2]

    if row["Unit_index"] == "219":
        print("Most abundant")
        for i in range(len(points)):
            print(points[i])

    for i in range(len(points)):
        row.update(utils_func.update_row_group(GROUPS[i], row, points[i]))

    return row


def update_second_most_abundant(row, group):
    points = []
    if group["name"] == "Fluvial":
        points = [1, 0, 0, 0, 0, -2]

    if group["name"] == "Shallow_Lacustrine":
        points = [0, 1, 0, 0, -1, -2]

    if group["name"] == "Deep_Lacustrine":
        points = [0, 0, 1, 1, -2, -2]

    if group["name"] == "Marginal_Marine":
        points = [0, 0, 1, 1, 0, -1]

    if group["name"] == "Shallow_Marine":
        points = [0, -1, -2, 0, 1, 0]

    if group["name"] == "Deep_Marine":
        points = [-2, -2, -2, -1, 0, 1]

    if row["Unit_index"] == "219":
        print("second abundant")
        for i in range(len(points)):
            print(points[i])

    for i in range(len(points)):
        row.update(utils_func.update_row_group(GROUPS[i], row, points[i]))

    return row


def update_third_most_abundant(row, group):
    points = []
    if group["name"] == "Fluvial":
        points = [0, 0, 0, 0, 0, -1]

    if group["name"] == "Shallow_Lacustrine":
        points = [0, 0, 1, 0, 0, -1]

    if group["name"] == "Deep_Lacustrine":
        points = [0, 1, 0, 0, 0, -1]

    if group["name"] == "Marginal_Marine":
        points = [0, 0, 0, 0, 0, 0]

    if group["name"] == "Shallow_Marine":
        points = [0, 0, 0, 0, 0, 0]

    if group["name"] == "Deep_Marine":
        points = [-1, -1, -1, 0, 0, 0]

    if row["Unit_index"] == "219":
        print("third abundant")
        for i in range(len(points)):
            print(points[i])

    for i in range(len(points)):
        row.update(utils_func.update_row_group(GROUPS[i], row, points[i]))

    return row


def update_4_6_most_abundant(row, group):
    points = []
    if group["name"] == "Fluvial":
        points = [-2, 0, 0, 0, 0, 0]

    if group["name"] == "Shallow_Lacustrine":
        points = [0, -2, 0, 0, 0, 0]

    if group["name"] == "Deep_Lacustrine":
        points = [0, 0, -2, 0, 0, 0]

    if group["name"] == "Marginal_Marine":
        points = [0, 0, 0, -2, 0, 0]

    if group["name"] == "Shallow_Marine":
        points = [0, 0, 0, 0, -2, 0]

    if group["name"] == "Deep_Marine":
        points = [0, 0, 0, 0, 0, -2]

    if row["Unit_index"] == "219":
        print("fourth")
        for i in range(len(points)):
            print(points[i])

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


def main(input_file, iter):
    with open(input_file) as file:
        csv_reader = reader(file)
        headers = list(csv_reader)[0]
        if "Facies_group" not in headers:
            headers.append("Facies_group")

    with open(input_file) as i_file:
        dict_reader = DictReader(i_file, )
        data = list(dict_reader)

        simplified_data = simplify_data(data) if iter == 1 else data

        for row in reversed(simplified_data):
            groups = pick_group(divide_group(find_max_radius_30(row["Unit_index"], simplified_data)))
            tmp = []
            for item in groups:
                tmp.append(item["name"])
            if len(groups) > 0:
                row.update(update_row(row, groups))
                row.update({"Facies_group": tmp})

        utils_func.export_to_csv(f"../../csv/associated_facies{iter}.csv", simplified_data, headers)


for i in range(0, 2):
    if i == 0:
        main("../../csv/stacking_pattern.csv", i + 1)
    else:
        main(f"../../csv/upper_boundary{i}.csv", i + 1)
    lower_boundary.main(f"../../csv/associated_facies{i + 1}.csv", i + 1)
    upper_boundary.main(f"../../csv/lower_boundary{i + 1}.csv", i + 1)
