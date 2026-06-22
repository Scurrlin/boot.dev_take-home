def get_new_levels(heroes, min_level):
    return [(hero[0], hero[1] * 3) for hero in heroes if hero[1] * 3 >= min_level]
