def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    most_common = None

    for name in enemies_dict:
        if enemies_dict[name] > max_so_far:
            max_so_far = enemies_dict[name]
            most_common = name

    return most_common
