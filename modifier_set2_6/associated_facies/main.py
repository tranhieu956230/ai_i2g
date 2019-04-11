from csv import DictWriter, DictReader, reader

names = [
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
    "Tidal_Channel_And_Sand_Flat",
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


def find_max_curve(row):
    max = 0
    lst = []
    for name in names:
        if int(row[name]) > max:
            max = int(row[name])

    if max > 0:
        for name in names:
            if int(row[name]) == max:
                lst.append(name)
        print(max)
    return lst

def get_radius_30():



with open("../../modifier_set1_5/stacking_pattern/stacking_pattern.csv") as i_file:
    dict_reader = DictReader(i_file)
    data = list(dict_reader)
    for row in data:
        if len(find_max_curve(row)) > 0:
            print(find_max_curve(row))
