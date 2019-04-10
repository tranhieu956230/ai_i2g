from modifier_set1_5.stacking_pattern import update_point
from csv import DictReader, DictWriter, reader

with open("../vertical_proximity/vertical_proximity.csv") as csv_file:
    csv_reader = list(reader(csv_file))
    headers = csv_reader[0]

with open("../vertical_proximity/vertical_proximity.csv") as csv_file:
    data = DictReader(csv_file)
    with open("stacking_pattern.csv", "w") as write_file:
        writer = DictWriter(write_file, fieldnames=headers)
        writer.writeheader()

        for row in data:
            row.update(update_point.update_fluvial(row))
            row.update(update_point.update_deep_lacustrine(row))
            row.update(update_point.update_deep_marine(row))
            row.update(update_point.update_marginal_marine(row))
            row.update(update_point.update_shallow_lacustrine(row))
            row.update(update_point.update_shallow_marine(row))

            writer.writerow(row)
