def init_alluvial_fan(data_set):
    if data_set["Lithofacies_major"] == "1" and data_set["GR_shape_code"] == "4":
        u_thick = float(data_set["Unit_Thick"])
        if 2 <= u_thick < 10:
            if u_thick >= 7:
                return 5
            elif u_thick >= 4:
                return 4
            else:
                return 3
    return 0


def init_marine_fan_delta(data_set):
    if data_set["Lithofacies_major"] == "1" and data_set["GR_shape_code"] == "4":
        u_thick = float(data_set["Unit_Thick"])
        if 2 <= u_thick < 15:
            if u_thick >= 10:
                return 6
            elif u_thick >= 5:
                return 5
            else:
                return 4
    return 0


def init_lacustrine_fan_delta(data_set):
    if data_set["Lithofacies_major"] == "1" and data_set["GR_shape_code"] == "4":
        u_thick = float(data_set["Unit_Thick"])
        if 2 <= u_thick < 15:
            if u_thick >= 10:
                return 6
            elif u_thick >= 5:
                return 5
            else:
                return 4
    return 0


def init_marine_delta(data_set):
    if data_set["Lithofacies_major"] == "1" and data_set["GR_shape_code"] == "4":
        u_thick = float(data_set["Unit_Thick"])
        if 2 <= u_thick < 15:
            if u_thick >= 10:
                return 7
            elif u_thick >= 5:
                return 6
            else:
                return 5
    return 0


def init_progradational_lacustrine_delta(data_set):
    if data_set["Lithofacies_major"] == "1" and data_set["GR_shape_code"] == "4":
        u_thick = float(data_set["Unit_Thick"])
        if 2 <= u_thick < 15:
            if u_thick >= 10:
                return 7
            elif u_thick >= 5:
                return 6
            else:
                return 5
    return 0


def init_progradational_marine_shoreface(data_set):
    if data_set["Lithofacies_major"] == "1" and data_set["GR_shape_code"] == "4":
        u_thick = float(data_set["Unit_Thick"])
        if 2 <= u_thick < 10:
            if u_thick >= 7:
                return 5
            elif u_thick >= 5:
                return 6
            else:
                return 4
    return 0


def init_progradational_lacustrine_shoreface(data_set):
    if data_set["Lithofacies_major"] == "1" and data_set["GR_shape_code"] == "4":
        u_thick = float(data_set["Unit_Thick"])
        if 2 <= u_thick < 10:
            if u_thick >= 7:
                return 5
            elif u_thick >= 5:
                return 6
            else:
                return 4
    return 0


def init_proximal_sub_lacustrine_fan(data_set):
    if data_set["Lithofacies_major"] == "1" and data_set["GR_shape_code"] == "4":
        u_thick = float(data_set["Unit_Thick"])
        if 10 <= u_thick < 30:
            if u_thick >= 22:
                return 6
            elif u_thick >= 15:
                return 5
            else:
                return 4
    return 0


def init_proximal_submarine_fan(data_set):
    if data_set["Lithofacies_major"] == "1" and data_set["GR_shape_code"] == "4":
        u_thick = float(data_set["Unit_Thick"])
        if 10 <= u_thick < 50:
            if u_thick >= 25:
                return 7
            elif u_thick >= 15:
                return 6
            else:
                return 5
    return 0


def init_fluvial_channel(data_set):
    if data_set["Lithofacies_major"] == "1" and data_set["GR_shape_code"] == "1":
        u_thick = float(data_set["Unit_Thick"])
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                return 5
            elif u_thick >= 3:
                return 6
            else:
                return 3
    return 0


def init_fluvial_point_bar(data_set):
    if data_set["Lithofacies_major"] == "1" and data_set["GR_shape_code"] == "1":
        u_thick = float(data_set["Unit_Thick"])
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                return 5
            elif u_thick >= 3:
                return 6
            else:
                return 3
    return 0


def init_levee(data_set):
    if data_set["Lithofacies_major"] == "1" and data_set["GR_shape_code"] == "1":
        u_thick = float(data_set["Unit_Thick"])
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                return 2
            elif u_thick >= 3:
                return 3
            else:
                return 4
    return 0


def init_crevasse_splay(data_set):
    if data_set["Lithofacies_major"] == "1" and data_set["GR_shape_code"] == "1":
        u_thick = float(data_set["Unit_Thick"])
        if 1 <= u_thick < 5:
            if u_thick >= 4:
                return 2
            elif u_thick >= 2:
                return 3
            else:
                return 5
    return 0


def init_tidal_channel_and_sand_flat(data_set):
    if data_set["Lithofacies_major"] == "1" and data_set["GR_shape_code"] == "1":
        u_thick = float(data_set["Unit_Thick"])
        if 1 <= u_thick < 5:
            if u_thick >= 4:
                return 3
            elif u_thick >= 2:
                return 4
            else:
                return 5
    return 0


def init_transgressive_lacustrine_shoreface(data_set):
    if data_set["Lithofacies_major"] == "1" and data_set["GR_shape_code"] == "1":
        u_thick = float(data_set["Unit_Thick"])
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                return 4
            elif u_thick >= 3:
                return 6
            else:
                return 3
    return 0


def init_transgressive_marine_shoreface(data_set):
    if data_set["Lithofacies_major"] == "1" and data_set["GR_shape_code"] == "1":
        u_thick = float(data_set["Unit_Thick"])
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                return 4
            elif u_thick >= 3:
                return 6
            else:
                return 3
    return 0


def init_lacustrine_turbidite(data_set):
    if data_set["Lithofacies_major"] == "1" and data_set["GR_shape_code"] == "1":
        u_thick = float(data_set["Unit_Thick"])
        if 1 <= u_thick < 5:
            if u_thick >= 4:
                return 2
            elif u_thick >= 2:
                return 3
            else:
                return 4
    return 0


def init_marine_turbidite(data_set):
    if data_set["Lithofacies_major"] == "1" and data_set["GR_shape_code"] == "1":
        u_thick = float(data_set["Unit_Thick"])
        if 1 <= u_thick < 10:
            if u_thick >= 7:
                return 3
            elif u_thick >= 3:
                return 4
            else:
                return 5
    return 0
