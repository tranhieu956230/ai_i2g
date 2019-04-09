from csv import DictReader, DictWriter, reader
from prepare_data import unit_matching

with open("data.csv") as csv_file:
    csv_reader = list(reader(csv_file))
    headers = csv_reader[0]

with open("data.csv") as csv_file:
    data = DictReader(csv_file)
    data = list(data)
    with open("prepared_data.csv", "w") as write_file:
        headers.extend(["Unit_Thick"])
        writer = DictWriter(write_file, fieldnames=headers)
        writer.writeheader()
        bound = 0
        for i in range(len(data) - 1):
            if data[i]["Unit_index"] != data[i+1]["Unit_index"]:
                unit_length = float(data[i]["TVD"]) - float(data[bound]["TVD"])
                idx = bound + 1 if bound > 0 else 0
                data[idx].update({"Unit_Thick": unit_length})
                writer.writerow(data[idx])
                bound = i








