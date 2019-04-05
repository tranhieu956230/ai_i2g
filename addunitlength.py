from csv import DictReader, DictWriter, reader

with open("data.csv") as csv_file:
    csv_reader = list(reader(csv_file))
    headers = csv_reader[0]

with open("data.csv") as csv_file:
    data = DictReader(csv_file)
    data = list(data)
    with open("unit_thick.csv", "w") as write_file:
        headers.extend(["Unit_Thick"])
        writer = DictWriter(write_file, fieldnames=headers)
        writer.writeheader()
        first = 0
        for i in range(len(data) - 1):
            if data[i]["Unit_index"] != data[i+1]["Unit_index"]:
                unit_length = float(data[i]["TVD"]) - float(data[first]["TVD"])
                for j in range(first, i + 1):
                    data[j].update({"Unit_Thick": unit_length})
                    writer.writerow(data[j])
                first = i + 1








