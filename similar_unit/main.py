from csv import DictReader, DictWriter, reader
from utilites import utils_func

def find_unit_core_depofacies(unit_index, data_list):
    depofacies = []
    for row in data_list:
        if row["Unit_index"] in unit_index:
            depofacies.append(row["Core_depofacies"])
    return utils_func.removeDuplicate(depofacies)

def handle_point(current_point, radius):
    current_point = int(current_point)
    if current_point == 0:
        current_point = 5
    elif radius == "0-50":
        current_point += 4
    elif radius == "50-100":
        current_point += 2
    return current_point


with open("../initial_point/init_point.csv") as file:
    csv_reader = reader(file)
    headers = list(csv_reader)[0]

with open("../initial_point/init_point.csv") as file:
    dict_reader = DictReader(file)
    data = list(dict_reader)
    for i in range(len(data)):
        if data[i]["Number_of_similar_units_50"] != "0":
            unit_index = utils_func.convert_string_to_array(data[i]["Index_of_similar_units_50"])
            idx = data[i]["Unit_index"]
            unit_index.append(idx)
            codes = find_unit_core_depofacies(unit_index, data)
            for code in codes:
                name = utils_func.map_core_depofacies_code_to_name(code)
                if name:
                    new_point = handle_point(data[i][name], "0-50")
                    print(new_point)
                    data[i].update({name: new_point})

        if data[i]["Number_of_similar_units_100"] != "0":
            unit_index = utils_func.convert_string_to_array(data[i]["Index_of_similar_units_100"])
            codes = find_unit_core_depofacies(unit_index, data)
            for code in codes:
                name = utils_func.map_core_depofacies_code_to_name(code)
                if name:
                    new_point = handle_point(data[i][name], "50-100")
                    print(new_point)
                    data[i].update({name: new_point})


with open("similar_unit.csv", "w") as new_file:
    dict_writer = DictWriter(new_file, fieldnames=headers)
    dict_writer.writeheader()
    for row in data:
        dict_writer.writerow(row)
