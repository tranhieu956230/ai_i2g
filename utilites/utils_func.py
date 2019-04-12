from csv import DictWriter
from copy import deepcopy
from collections import Counter


def remove_duplicate(arr):
    arr.sort()
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            arr.pop(i)
            i -= 1
        i += 1
    return arr


def map_core_depofacies_code_to_name(code):
    try:
        code_to_name = {
            "1.1": "Alluvial_Fan",
            "1.2": "Fluvial_Channel",
            "1.3": "Fluvial_Point_Bar",
            "1.4": "Levee",
            "1.5": "Crevasse_Splay",
            "1.6": "Fluvial_Floodplain",
            "2.1": "Progradational_Lacustrine_Delta",
            "2.2": "Lacustrine_Fan_Delta",
            "2.3": "Progradational_Lacustrine_Shoreface",
            "2.4": "Transgressive_Lacustrine_Shoreface",
            "2.5": "Aggradational_Lacustrine_Shoreface",
            "2.6": "Lacustrine_Offshore_Transition",
            "2.7": "Lacustrine_Shelf",
            "3.1": "Proximal_Sub-Lacustrine_Fan",
            "3.2": "Distal_Sub-Lacustrine_Fan",
            "3.3": "Lacustrine_Turbidite",
            "3.4": "Distal_Lacustrine_Turbidites",
            "3.5": "Lacustrine_Deepwater",
            "4.1": "Marine_Delta",
            "4.2": "Marine_Fan_Delta",
            "4.3": "Tidal_Channel_And_Sand_Flat",
            "4.4": "Sandy_Tidal_Flat",
            "4.5": "Mixed_Tidal_Flat",
            "4.6": "Muddy_Tidal_Flat",
            "4.7": "Lagoon",
            "5.1": "Progradational_Marine_Shoreface",
            "5.2": "Transgressive_Marine_Shoreface",
            "5.3": "Aggradational_Marine_Shoreface",
            "5.4": "Marine_Offshore_Transition",
            "5.5": "Marine_Shelf",
            "6.1": "Proximal_Submarine_Fan",
            "6.2": "Distal_Submarine_Fan",
            "6.3": "Marine_Turbidite",
            "6.4": "Distal_Marine_Turbidites",
            "6.5": "Marine_Deepwater"
        }
        return code_to_name[code]
    except KeyError:
        return None


def convert_string_to_array(string):
    return string[1:-1].split(", ") if string != '[]' else []


def get_group_depofacies(name):
    try:
        groups = {
            "Fluvial": ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6"],
            "Shallow_Lacustrine": ["2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7"],
            "Deep_Lacustrine": ["3.1", "3.2", "3.3", "3.4", "3.5"],
            "Marginal_Marine": ["4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7"],
            "Shallow_Marine": ["5.1", "5.2", "5.3", "5.4", "5.5"],
            "Deep_Marine": ["6.1", "6.2", "6.3", "6.4", "6.5"]
        }
        return groups[name]
    except KeyError:
        return None


def get_group_name(facy_name):
    code_to_name = {
        "1.1": "Alluvial_Fan",
        "1.2": "Fluvial_Channel",
        "1.3": "Fluvial_Point_Bar",
        "1.4": "Levee",
        "1.5": "Crevasse_Splay",
        "1.6": "Fluvial_Floodplain",
        "2.1": "Progradational_Lacustrine_Delta",
        "2.2": "Lacustrine_Fan_Delta",
        "2.3": "Progradational_Lacustrine_Shoreface",
        "2.4": "Transgressive_Lacustrine_Shoreface",
        "2.5": "Aggradational_Lacustrine_Shoreface",
        "2.6": "Lacustrine_Offshore_Transition",
        "2.7": "Lacustrine_Shelf",
        "3.1": "Proximal_Sub-Lacustrine_Fan",
        "3.2": "Distal_Sub-Lacustrine_Fan",
        "3.3": "Lacustrine_Turbidite",
        "3.4": "Distal_Lacustrine_Turbidites",
        "3.5": "Lacustrine_Deepwater",
        "4.1": "Marine_Delta",
        "4.2": "Marine_Fan_Delta",
        "4.3": "Tidal_Channel_And_Sand_Flat",
        "4.4": "Sandy_Tidal_Flat",
        "4.5": "Mixed_Tidal_Flat",
        "4.6": "Muddy_Tidal_Flat",
        "4.7": "Lagoon",
        "5.1": "Progradational_Marine_Shoreface",
        "5.2": "Transgressive_Marine_Shoreface",
        "5.3": "Aggradational_Marine_Shoreface",
        "5.4": "Marine_Offshore_Transition",
        "5.5": "Marine_Shelf",
        "6.1": "Proximal_Submarine_Fan",
        "6.2": "Distal_Submarine_Fan",
        "6.3": "Marine_Turbidite",
        "6.4": "Distal_Marine_Turbidites",
        "6.5": "Marine_Deepwater"
    }

    groups = {
        "Fluvial": ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6"],
        "Shallow_Lacustrine": ["2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7"],
        "Deep_Lacustrine": ["3.1", "3.2", "3.3", "3.4", "3.5"],
        "Marginal_Marine": ["4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7"],
        "Shallow_Marine": ["5.1", "5.2", "5.3", "5.4", "5.5"],
        "Deep_Marine": ["6.1", "6.2", "6.3", "6.4", "6.5"]
    }

    for key, item in code_to_name.items():
        if item == facy_name:
            facy_code = key

    for key, item in groups.items():
        if facy_code in item:
            return key


def get_max_by_key(key, data):
    lst = []
    max = 0
    for item in data:
        if int(item[key]) > max:
            max = item[key]
    for item in data:
        if int(item[key]) == max:
            lst.append(item)
    return lst


def update_row_group(group_name, row, point):
    for depofacy in get_group_depofacies(group_name):
        name = map_core_depofacies_code_to_name(depofacy)
        if int(row[name]) > 0:
            if point == "x":
                row.update({name: 0})
            else:
                row.update({name: int(row[name]) + point})
    return row


def convert_unit_by_unit(data):
    lst = []
    lithos = []
    depos = []
    for i in range(0, len(data)):
        if data[i]["Special_lithology"] != "-999":
            lithos.append(float(data[i]["Special_lithology"]))
        if data[i]["Core_depofacies"] != "-999":
            depos.append((float(data[i]["Core_depofacies"])))
        if data[i]["Boundary_flag"] == "1":
            final_litho = deepcopy(remove_duplicate(lithos))
            final_depos = deepcopy(remove_duplicate(depos))
            data[i].update({"Special_lithology": final_litho, "Core_depofacies": final_depos})
            lst.append(data[i])
            lithos.clear()
            depos.clear()

    return lst


def export_to_csv(filename, data):
    headers = data[0].keys()
    with open(filename, "w") as o_file:
        csv_writer = DictWriter(o_file, fieldnames=headers)
        csv_writer.writeheader()
        for row in data:
            csv_writer.writerow(row)


def pick_most(data):
    if len(data) == 0:
        return None
    return sorted(data, key=Counter(data).get, reverse=True)[0]


def handle_addition(point):
    if int(point) <= 0:
        return 0
    return int(point)
