from csv import DictReader, reader
from utilites import utils_func
from modifier_set1_5.biostratigraphy import update_point

with open("../../special_lithology_4/special_lithology.csv") as file:
    reader = reader(file)
    headers = list(reader)[0]

with open("../../special_lithology_4/special_lithology.csv") as i_file:
    dict_reader = DictReader(i_file)
    data = list(dict_reader)
    for row in data:
        row.update(update_point.update_fluvial(row))
        row.update(update_point.update_shallow_lacustrine(row))
        row.update(update_point.update_deep_lacustrine(row))
        row.update(update_point.update_marginal_marine(row))
        row.update(update_point.update_shallow_marine(row))
        row.update(update_point.update_deep_marine(row))

utils_func.export_to_csv("biostratigraphy.csv", data)

utils_func.export_to_csv("biostratigraphy_unit_by_unit.csv", utils_func.convert_unit_by_unit(data))
