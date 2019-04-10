from csv import DictReader, DictWriter, reader

groups = {
    "Fluvial": ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6"],
    "Shallow_Lacustrine": ["2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7"],
    "Deep_Lacustrine": ["3.1", "3.2", "3.3", "3.4", "3.5"],
    "Marginal_Marine": ["4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7"],
    "Shallow_Marine": ["5.1", "5.2", "5.3", "5.4", "5.5"],
    "Deep_Marine": ["6.1", "6.2", "6.3", "6.4", "6.5"]
}


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
            "4.3": "Tidal_Channel_and_Sand_Flat",
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


def add_point_volcanics(row):
    return row


def add_point_marine_non_clastic(row):
    marines = ["Shallow_Marine", "Marginal_Marine", "Deep_Marine"]
    for group_name in marines:
        for code in groups[group_name]:
            name = map_core_depofacies_code_to_name(code)
            if int(row[name]) > 0:
                row.update({name: int(row[name]) + 2})
    return row


def add_point_coal(row):
    for code in groups["Fluvial"]:
        name = map_core_depofacies_code_to_name(code)
        if int(row[name]) > 0:
            row.update({name: int(row[name]) + 2})

    for code in groups["Marginal_Marine"]:
        name = map_core_depofacies_code_to_name(code)
        if int(row[name]) > 0:
            row.update({name: int(row[name]) + 1})

    return row


def updateRow(row, litho_code):
    litho_code = int(litho_code)
    if litho_code in [1, 2]:
        return add_point_volcanics(row)
    if litho_code in range(3, 8):
        return add_point_marine_non_clastic(row)
    if litho_code == 8:
        return add_point_coal(row)
    return row


def find_unit_special_lithology(unit_index, data):
    lithologies = []
    for row in data:
        if int(row["Unit_index"]) == int(unit_index) and row["Special_lithology"] != '-999':
            lithologies.append(row["Special_lithology"])
    return lithologies


def removeDuplicate(arr):
    arr.sort()
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            arr.pop(i)
            i -= 1
        i += 1
    return arr


def find_adjacent_unit_special_lithology(unit_index, data):
    before = find_unit_special_lithology(int(unit_index) - 1, data)
    current = find_unit_special_lithology(int(unit_index), data)
    after = find_unit_special_lithology(int(unit_index) + 1, data)
    before.extend(current)
    before.extend(after)
    return removeDuplicate(before)


with open("../similar_unit/similar_unit.csv") as i_file:
    csv_reader = reader(i_file)
    headers = list(csv_reader)[0]

with open("../similar_unit/similar_unit.csv") as i_file:
    dict_reader = DictReader(i_file)
    data = list(dict_reader)
    for i in range(len(data)):
        lithologies = find_adjacent_unit_special_lithology(data[i]["Unit_index"], data)
        if len(lithologies) > 0:
            for lithology in lithologies:
                print(lithology)
                data[i].update(updateRow(data[i], lithology))

with open("special_lithology.csv", "w") as o_file:
    dict_writer = DictWriter(o_file, fieldnames=headers)
    dict_writer.writeheader()
    for row in data:
        dict_writer.writerow(row)
