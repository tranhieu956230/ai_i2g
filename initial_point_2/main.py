from initial_point_2 import initpoint
from utilites import utils_func
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

with open("../prepare_data_1/prepare_data.csv") as csv_file:
    csv_reader = list(reader(csv_file))
    headers = csv_reader[0]

with open("../prepare_data_1/prepare_data.csv") as csv_file:
    csv_reader = DictReader(csv_file)
    data = list(csv_reader)
    with open("init_point.csv", "w") as write_file:
        headers.extend(additional)
        writer = DictWriter(write_file, fieldnames=headers)
        writer.writeheader()

        for row in data:
            row.update({
                "Alluvial_Fan": initpoint.init_alluvial_fan(row),
                "Fluvial_Channel": initpoint.init_fluvial_channel(row),
                "Fluvial_Point_Bar": initpoint.init_fluvial_point_bar(row),
                "Levee": initpoint.init_levee(row),
                "Crevasse_Splay": initpoint.init_crevasse_splay(row),
                "Fluvial_Floodplain": initpoint.init_fluvial_floodplain(row),
                "Progradational_Lacustrine_Delta": initpoint.init_progradational_lacustrine_delta(row),
                "Lacustrine_Fan_Delta": initpoint.init_lacustrine_fan_delta(row),
                "Progradational_Lacustrine_Shoreface": initpoint.init_progradational_lacustrine_shoreface(row),
                "Transgressive_Lacustrine_Shoreface": initpoint.init_transgressive_lacustrine_shoreface(row),
                "Aggradational_Lacustrine_Shoreface": initpoint.init_aggradational_lacustrine_shoreface(row),
                "Lacustrine_Offshore_Transition": initpoint.init_lacustrine_offshore_transition(row),
                "Lacustrine_Shelf": initpoint.init_lacustrine_shelf(row),
                "Proximal_Sub-Lacustrine_Fan": initpoint.init_proximal_sub_lacustrine_fan(row),
                "Distal_Sub-Lacustrine_Fan": initpoint.init_distal_sub_lacustrine_fan(row),
                "Lacustrine_Turbidite": initpoint.init_lacustrine_turbidite(row),
                "Distal_Lacustrine_Turbidites": initpoint.init_distal_lacustrine_turbidites(row),
                "Lacustrine_Deepwater": initpoint.init_lacustrine_deepwater(row),
                "Marine_Delta": initpoint.init_marine_delta(row),
                "Marine_Fan_Delta": initpoint.init_marine_fan_delta(row),
                "Tidal_Channel_And_Sand_Flat": initpoint.init_tidal_channel_and_sand_flat(row),
                "Sandy_Tidal_Flat": initpoint.init_sandy_tidal_flat(row),
                "Mixed_Tidal_Flat": initpoint.init_mixed_tidal_flat(row),
                "Muddy_Tidal_Flat": initpoint.init_muddy_tidal_flat(row),
                "Lagoon": initpoint.init_lagoon(row),
                "Progradational_Marine_Shoreface": initpoint.init_progradational_marine_shoreface(row),
                "Transgressive_Marine_Shoreface": initpoint.init_transgressive_marine_shoreface(row),
                "Aggradational_Marine_Shoreface": initpoint.init_aggradational_marine_shoreface(row),
                "Marine_Offshore_Transition": initpoint.init_marine_offshore_transition(row),
                "Marine_Shelf": initpoint.init_marine_shelf(row),
                "Proximal_Submarine_Fan": initpoint.init_proximal_submarine_fan(row),
                "Distal_Submarine_Fan": initpoint.init_distal_submarine_fan(row),
                "Marine_Turbidite": initpoint.init_marine_turbidite(row),
                "Distal_Marine_Turbidites": initpoint.init_distal_marine_turbidites(row),
                "Marine_Deepwater": initpoint.init_marine_deepwater(row)})
            writer.writerow(row)


utils_func.export_to_csv("init_point_unit_by_unit.csv", utils_func.convert_unit_by_unit(data))