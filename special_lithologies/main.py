from csv import DictReader, DictWriter, reader
from utilites import utils_func

def add_point_volcanics(row):
    return row

def add_point_marine_non_clastic(row):
    marines = ["Shallow_Marine", "Marginal_Marine", "Deep_Marine"]
    for group_name in marines:
        codes = utils_func.get_group_depofacies(group_name)
        for code in codes:
            name = utils_func.map_core_depofacies_code_to_name(code)
            if int(row[name]) > 0:
                row.update({name: int(row[name]) + 2})
    return row


def add_point_coal(row):
    for code in utils_func.get_group_depofacies("Fluvial"):
        name = utils_func.map_core_depofacies_code_to_name(code)
        if int(row[name]) > 0:
            row.update({name: int(row[name]) + 2})

    for code in utils_func.get_group_depofacies("Marginal_Marine"):
        name = utils_func.map_core_depofacies_code_to_name(code)
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


def find_adjacent_unit_special_lithology(unit_index, data):
    before = find_unit_special_lithology(int(unit_index) - 1, data)
    current = find_unit_special_lithology(int(unit_index), data)
    after = find_unit_special_lithology(int(unit_index) + 1, data)
    before.extend(current)
    before.extend(after)
    return utils_func.removeDuplicate(before)


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
