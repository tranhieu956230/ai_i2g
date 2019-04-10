from csv import DictWriter, DictReader, reader
from modifier_set_1 import set_point

with open("../special_lithologies/special_lithology.csv") as file:
    reader = reader(file)
    headers = list(reader)[0]


with open("../special_lithologies/special_lithology.csv") as i_file:
    dict_reader = DictReader(i_file)
    data = list(dict_reader)
    for row in data:
        row.update(set_point.update_fluvial(row))
        row.update(set_point.update_shallow_lacustrine(row))
        row.update(set_point.update_deep_lacustrine(row))
        row.update(set_point.update_marginal_marine(row))
        row.update(set_point.update_shallow_marine(row))
        row.update(set_point.update_deep_marine(row))


with open("biostratigraphy.csv", "w") as o_file:
    csv_writer = DictWriter(o_file, fieldnames=headers)
    csv_writer.writeheader()
    for row in data:
        csv_writer.writerow(row)


