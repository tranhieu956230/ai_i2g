from csv import DictReader, DictWriter, reader
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
        for i in range(len(data) - 1):
            if data[i]["Unit_index"] != data[i+1]["Unit_index"]:
                unit_thick = float(data[i]["TVD"]) - float(data[bound]["TVD"])
                for j in range(bound + 1 if bound > 0 else 0, i + 1):
                    data[j].update({"Unit_Thick": unit_thick})
                    writer.writerow(data[j])
                bound = i








