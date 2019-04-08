from initpoint import *
from csv import DictReader, DictWriter, reader

additional = [
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
    with open("init_point.csv", "w") as write_file:
        headers.extend(additional)
        writer = DictWriter(write_file, fieldnames=headers)
        writer.writeheader()

        for row in data:
            row.update({
                "Alluvial_Fan": init_alluvial_fan(row),
                "Fluvial_Channel": init_fluvial_channel(row),
                "Fluvial_Point_Bar": init_fluvial_point_bar(row),
                "Levee": init_levee(row),
                "Crevasse_Splay": init_crevasse_splay(row),
                "Fluvial_Floodplain": init_fluvial_floodplain(row),
                "Progradational_Lacustrine_Delta": init_progradational_lacustrine_delta(row),
                "Lacustrine_Fan_Delta": init_lacustrine_fan_delta(row),
                "Progradational_Lacustrine_Shoreface": init_progradational_lacustrine_shoreface(row),
                "Transgressive_Lacustrine_Shoreface": init_transgressive_lacustrine_shoreface(row),
                "Aggradational_Lacustrine_Shoreface": init_aggradational_lacustrine_shoreface(row),
                "Lacustrine_Offshore_Transition": init_lacustrine_offshore_transition(row),
                "Lacustrine_Shelf": init_lacustrine_shelf(row),
                "Proximal_Sub-Lacustrine_Fan": init_proximal_sub_lacustrine_fan(row),
                "Distal_Sub-Lacustrine_Fan": init_distal_sub_lacustrine_fan(row),
                "Lacustrine_Turbidite": init_lacustrine_turbidite(row),
                "Distal_Lacustrine_Turbidites": init_distal_lacustrine_turbidites(row),
                "Lacustrine_Deepwater": init_lacustrine_deepwater(row),
                "Marine_Delta": init_marine_delta(row),
                "Marine_Fan_Delta": init_marine_fan_delta(row),
                "Tidal_Channel_and_Sand_Flat": init_tidal_channel_and_sand_flat(row),
                "Sandy_Tidal_Flat": init_sandy_tidal_flat(row),
                "Mixed_Tidal_Flat": init_mixed_tidal_flat(row),
                "Muddy_Tidal_Flat": init_muddy_tidal_flat(row),
                "Lagoon": init_lagoon(row),
                "Progradational_Marine_Shoreface": init_progradational_marine_shoreface(row),
                "Transgressive_Marine_Shoreface": init_transgressive_marine_shoreface(row),
                "Aggradational_Marine_Shoreface": init_aggradational_marine_shoreface(row),
                "Marine_Offshore_Transition": init_marine_offshore_transition(row),
                "Marine_Shelf": init_marine_shelf(row),
                "Proximal_Submarine_Fan": init_proximal_submarine_fan(row),
                "Distal_Submarine_Fan": init_distal_submarine_fan(row),
                "Marine_Turbidite": init_marine_turbidite(row),
                "Distal_Marine_Turbidites": init_distal_marine_turbidites(row),
                "Marine_Deepwater": init_marine_deepwater(row)})
            writer.writerow(row)
