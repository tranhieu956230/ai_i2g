from initpoint import init_alluvial_fan
from csv import DictReader, DictWriter, reader

headers = [
    "Alluvial_Fan",
    "Fluvial_Channel",
    "Fluvial_Point_Bar",
    "Levee",
    "Crevasse_Splay",
    "Fluvial_Floodplain",
    "Progradational_Lacustrine_Delta",
    "Lacustrine_Fan_Delta",
    "Progradational_Lacustrine_Shoreface",
    "Transgressive_Lacustrine_Shoreface",
    "Aggradational_Lacustrine_Shoreface",
    "Lacustrine_Offshore_Transition",
    "Lacustrine_Shelf",
    "Proximal_Sub-Lacustrine_Fan",
    "Distal_Sub-Lacustrine_Fan",
    "Lacustrine_Turbidite",
    "Distal_Lacustrine_Turbidites",
    "Lacustrine_Deepwater",
    "Marine_Delta",
    "Marine_Fan_Delta",
    "Tidal_Channel_and_Sand_Flat",
    "Sandy_Tidal_Flat",
    "Mixed_Tidal_Flat",
    "Muddy_Tidal_Flat",
    "Lagoon",
    "Progradational_Marine_Shoreface",
    "Transgressive_Marine_Shoreface",
    "Aggradational_Marine_Shoreface",
    "Marine_Offshore_Transition",
    "Marine_Shelf",
    "Proximal_Submarine_Fan",
    "Distal_Submarine_Fan",
    "Marine_Turbidite",
    "Distal_Marine_Turbidites",
    "Marine_Deepwater"
]

with open("unit_thick.csv") as csv_file:
    csv_reader = list(reader(csv_file))
    headers = csv_reader[0]

with open("unit_thick.csv") as csv_file:
    data = DictReader(csv_file)
    with open("initial_point.csv", "w") as write_file:
        writer = DictWriter(write_file, fieldnames=headers)
        writer.writeheader()

        for row in data:
            row.update({"Alluvial_Fan": init_alluvial_fan(row)})
            writer.writerow(row)
