def get_idx(number_of_similar_unit):
    number_of_similar_unit = int(number_of_similar_unit)
    if number_of_similar_unit == 0:
        return 0
    elif number_of_similar_unit in [1, 2]:
        return 1
    elif number_of_similar_unit in [3, 4, 5]:
        return 2
    elif number_of_similar_unit > 5:
        return 3


def update_alluvial_fan(data_set):
    if data_set["Alluvial_Fan"] == "0":
        return 0
    points = [-1, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_fluvial_channel(data_set):
    if data_set["Fluvial_Channel"] == "0":
        return 0
    points = [-2, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_fluvial_point_bar(data_set):
    if data_set["Fluvial_Point_Bar"] == "0":
        return 0
    points = [-2, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_levee(data_set):
    if data_set["Levee"] == "0":
        return 0
    points = [-1, 1, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_crevasse_splay(data_set):
    if data_set["Crevasse_Splay"] == "0":
        return 0
    points = [-1, 1, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_fluvial_floodplain(data_set):
    if data_set["Fluvial_Floodplain"] == "0":
        return 0
    points = [-3, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_progradational_lacustrine_delta(data_set):
    if data_set["Progradational_Lacustrine_Delta"] == "0":
        return 0
    points = [-3, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_lacustrine_fan_delta(data_set):
    if data_set["Lacustrine_Fan_Delta"] == "0":
        return 0
    points = [-2, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_progradational_lacustrine_shoreface(data_set):
    if data_set["Progradational_Lacustrine_Shoreface"] == "0":
        return 0
    points = [-2, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_transgressive_lacustrine_shoreface(data_set):
    if data_set["Transgressive_Lacustrine_Shoreface"] == "0":
        return 0
    points = [-1, 1, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_aggradational_lacustrine_shoreface(data_set):
    if data_set["Aggradational_Lacustrine_Shoreface"] == "0":
        return 0
    points = [-2, 1, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_lacustrine_offshore_transition(data_set):
    if data_set["Lacustrine_Offshore_Transition"] == "0":
        return 0
    points = [-1, 1, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_lacustrine_shelf(data_set):
    if data_set["Lacustrine_Shelf"] == "0":
        return 0
    points = [-2, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_proximal_sub_lacustrine_fan(data_set):
    if data_set["Proximal_Sub-Lacustrine_Fan"] == "0":
        return 0
    points = [-1, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_distal_sub_lacustrine_fan(data_set):
    if data_set["Distal_Sub-Lacustrine_Fan"] == "0":
        return 0
    points = [-1, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_lacustrine_turbidite(data_set):
    if data_set["Lacustrine_Turbidite"] == "0":
        return 0
    points = [-2, 1, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_distal_lacustrine_turbidites(data_set):
    if data_set["Distal_Lacustrine_Turbidites"] == "0":
        return 0
    points = [-2, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_lacustrine_deepwater(data_set):
    if data_set["Lacustrine_Deepwater"] == "0":
        return 0
    points = [-3, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_marine_delta(data_set):
    if data_set["Marine_Delta"] == "0":
        return 0
    points = [-3, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_marine_fan_delta(data_set):
    if data_set["Marine_Fan_Delta"] == "0":
        return 0
    points = [-2, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_tidal_channel_and_sand_flat(data_set):
    if data_set["Tidal_Channel_And_Sand_Flat"] == "0":
        return 0
    points = [-1, 1, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_sandy_tidal_flat(data_set):
    if data_set["Sandy_Tidal_Flat"] == "0":
        return 0
    points = [-1, 1, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_mixed_tidal_flat(data_set):
    if data_set["Mixed_Tidal_Flat"] == "0":
        return 0
    points = [-1, 1, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_muddy_tidal_flat(data_set):
    if data_set["Muddy_Tidal_Flat"] == "0":
        return 0
    points = [-1, 1, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_lagoon(data_set):
    if data_set["Lagoon"] == "0":
        return 0
    points = [-2, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_progradational_marine_shoreface(data_set):
    if data_set["Progradational_Marine_Shoreface"] == "0":
        return 0
    points = [-2, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_transgressive_marine_shoreface(data_set):
    if data_set["Transgressive_Marine_Shoreface"] == "0":
        return 0
    points = [-1, 1, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_aggradational_marine_shoreface(data_set):
    if data_set["Aggradational_Marine_Shoreface"] == "0":
        return 0
    points = [-2, 1, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_marine_offshore_transition(data_set):
    if data_set["Marine_Offshore_Transition"] == "0":
        return 0
    points = [-1, 1, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_marine_shelf(data_set):
    if data_set["Marine_Shelf"] == "0":
        return 0
    points = [-2, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_proximal_submarine_fan(data_set):
    if data_set["Proximal_Submarine_Fan"] == "0":
        return 0
    points = [-1, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_distal_submarine_fan(data_set):
    if data_set["Distal_Submarine_Fan"] == "0":
        return 0
    points = [-1, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_marine_turbidite(data_set):
    if data_set["Marine_Turbidite"] == "0":
        return 0
    points = [-2, 1, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_distal_marine_turbidites(data_set):
    if data_set["Distal_Marine_Turbidites"] == "0":
        return 0
    points = [-2, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]


def update_marine_deepwater(data_set):
    if data_set["Marine_Deepwater"] == "0":
        return 0
    points = [-3, 0, 2, 3]
    return points[get_idx(data_set["Number_of_similar_units_50"])]
