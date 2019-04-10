from csv import DictReader, DictWriter, reader


def find_unit_core_depofacies(unit_index, data_list):
    depofacies = []
    for row in data_list:
        if row["Unit_index"] in unit_index:
            depofacies.append(row["Core_depofacies"])
    return removeDuplicate(depofacies)


def convert_string_to_array(string):
    return string[1:-1].split(", ") if string != '[]' else []


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


def handle_point(current_point, radius):
    current_point = int(current_point)
    if current_point == 0:
        current_point = 5
    elif radius == "0-50":
        current_point += 4
    elif radius == "50-100":
        current_point += 2
    return current_point


def removeDuplicate(arr):
    arr.sort()
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            arr.pop(i)
            i -= 1
        i += 1
    return arr


with open("../initial_point/init_point.csv") as file:
    csv_reader = reader(file)
    headers = list(csv_reader)[0]

with open("../initial_point/init_point.csv") as file:
    dict_reader = DictReader(file)
    data = list(dict_reader)
    for i in range(len(data)):
        if map_core_depofacies_code_to_name(data[i]["Core_depofacies"]):
            unit_index = convert_string_to_array(data[i]["Index_of_similar_units_50"])
            idx = data[i]["Unit_index"]
            unit_index.append(idx)
            codes = find_unit_core_depofacies(unit_index, data)
            for code in codes:
                name = map_core_depofacies_code_to_name(code)
                if name:
                    new_point = handle_point(data[i][name], "0-50")
                    data[i].update({name: new_point})

        if map_core_depofacies_code_to_name(data[i]["Core_depofacies"]):
            unit_index = convert_string_to_array(data[i]["Index_of_similar_units_100"])
            codes = find_unit_core_depofacies(unit_index, data)
            for code in codes:
                name = map_core_depofacies_code_to_name(code)
                if name:
                    new_point = handle_point(data[i][name], "50-100")
                    data[i].update({name: new_point})


with open("similar_unit.csv", "w") as new_file:
    dict_writer = DictWriter(new_file, fieldnames=headers)
    dict_writer.writeheader()
    for row in data:
        dict_writer.writerow(row)
