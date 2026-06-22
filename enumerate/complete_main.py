def numbered_inventory(items):
    numbered_items = []

    for i, item in enumerate(items, start=1):
        numbered_items.append(f"{i}. {item}")

    return numbered_items
