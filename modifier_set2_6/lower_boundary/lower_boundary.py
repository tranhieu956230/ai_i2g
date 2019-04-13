from csv import DictReader, reader, DictWriter
from utilites import utils_func
from copy import deepcopy

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


def find_max_lower(unit_index, data):
    unit_index = int(unit_index)
    lst = []

    if unit_index == len(data) - 1 or len(
            utils_func.convert_string_to_array(data[unit_index]["Special_lithology"])) > 0:
        return lst

    lst.extend(find_max_curve(data[unit_index + 1]))

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
    if len(data) == 1:
        return data[0]
    return None


def update_row(row, group):
    points = []
    sharp_boundary = int(row["Sharp_boundary"])

    if group["name"] == "Fluvial":
        points = [[2, 2], [-1, -1], [-2, 0], [-1, 0], [-1, 0], ["x", -3]]

    if group["name"] == "Shadow_Lacustrine":
        points = [[-1, 0], [2, 2], [-1, -1], [0, 0], [0, 0], ["x", -3]]

    if group["name"] == "Deep_Lacustrine":
        points = [[-2, -1], [2, 1], [2, 2], ["x", -3], ["x", -3], ["x", -4]]

    if group["name"] == "Marginal_Marine":
        points = [["x", 0], ["x", -2], ["x", -2], [2, 2], [1, 1], [0, 0]]

    if group["name"] == "Shallow_Marine":
        points = [["x", -2], ["x", -2], ["x", "x"], [1, 1], [2, 2], [1, 1]]

    if group["name"] == "Deep_Marine":
        points = [["x", -3], ["x", "x"], ["x", "x"], [-1, 1], [1, 1], [2, 2]]

    for i in range(len(points)):
        row.update(utils_func.update_row_group(GROUPS[i], row, points[i][sharp_boundary]))

    return row


with open("../associated_facies/associated_facies2.csv") as file:
    reader = reader(file)
    headers = list(reader)[0]
    headers.append("Facies_below")

with open("../associated_facies/associated_facies2.csv") as i_file:
    dict_reader = DictReader(i_file)
    data = list(dict_reader)
    for i in range(0, 2):
        for row in reversed(data):
            group = pick_group(divide_group(find_max_lower(row["Unit_index"], data)))
            if group:
                row.update(update_row(row, group))
                row.update({"Facies_below": group["name"] if group else None})

        with open(f"lower_boundary{i + 1}.csv", "w") as o_file:
            dict_writer = DictWriter(o_file, fieldnames=headers)
            dict_writer.writeheader()
            for row in data:
                dict_writer.writerow(row)


