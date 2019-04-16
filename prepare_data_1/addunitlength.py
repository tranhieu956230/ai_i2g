from csv import DictReader, DictWriter, reader
from utilites import utils_func
from prepare_data_1 import unit_matching

with open("data.csv") as csv_file:
    csv_reader = list(reader(csv_file))
    headers = csv_reader[0]

with open("data.csv") as csv_file:
    dict_writer = DictReader(csv_file)
    data = list(dict_writer)
    with open("prepare_data.csv", "w") as write_file:
        headers.extend(["Unit_Thick"])
        writer = DictWriter(write_file, fieldnames=headers)
        writer.writeheader()
        bound = 0
        for i in range(len(data)):
            if data[i]["Boundary_flag"] == "1":
                unit_thick = float(data[i]["TVD"]) - float(data[bound]["TVD"])
                for j in range(bound + 1 if bound > 0 else 0, i + 1):
                    data[j].update({"Unit_Thick": unit_thick})
                    writer.writerow(data[j])
                bound = i

    utils_func.export_to_csv("prepare_data_unit_by_unit.csv", utils_func.convert_unit_by_unit(data), headers)







