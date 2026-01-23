import sys


def stats(diction: dict, count_items: int):
    print("=== Current Inventory ===")
    for key, value in diction.items():
        print(f"{key}: {value} units ({(value/count_items) * 100:.1f}%)")


def analysiste(diction: dict):
    count_items = 0
    count_keys = 0

    print("=== Inventory System Analysis ===")
    for value in diction.values():
        count_items += value

    for key in diction.keys():
        count_keys += 1
    print(f"Total items in inventory: {count_items}")
    print(f"Unique item types: {count_keys}\n")
    stats(diction, count_items)


def restock_needed(diction: dict):
    run_out_of_stock = []
    for key, value in diction.items():
        if value == 1:
            run_out_of_stock += [key]
    print(run_out_of_stock)


def process(args):

    dictio = {}
    total_items = 0
    total_keys = 0
    grouped = {"high": {}, "medium": {}, "low": {}}
    for arg in args:
        key, value = arg.split(":")
        dictio[key] = int(value)

    for name, quantity in dictio.items():
        if quantity == 1:
            grouped["low"][name] = quantity
        elif quantity == 2:
            grouped["medium"][name] = quantity
        else:
            grouped["high"][name] = quantity

    for x, y in dictio.items():
        total_items += y
        total_keys += 1
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {total_keys}\n")
    print("=== Current Inventory ===")
    for key in grouped.keys():
        for key, value in grouped[key].items():
            print(f"{key}: {value} units ({(value/total_items) * 100:.1f}%)",)

    print("\n=== Inventory Statistics ===")
    least = min(dictio.values())
    moore = max(dictio.values())

    for key, value in dictio.items():
        if value == moore:
            print(f"Most abundant: {key} ({value} units)")
            break
    print()
    for key, value in dictio.items():
        if value == least:
            print(f"Least abundant: {key} ({value} units)")
            break

    print("=== Item Categories ===")
    catego = {"Moderate": {}, "Scarce": {}}
    for name, value in dictio.items():
        if value >= 5:
            catego["Moderate"][name] = value
        else:
            catego["Scarce"][name] = value
    print(f"Moderate: {catego["Moderate"]}")
    print(f"Scarce: {catego["Scarce"]}\n")

    print("=== Management Suggestions ===")
    print(f"Restock needed: {list(grouped["low"].keys())}")
    print(f"Dictionary keys: {list(dictio)}")
    print(f"Dictionary values: {list(dictio.values())}")
    recherche = "sword"
    for name in dictio:
        if name == recherche:
            print(f"Sample lookup - '{recherche}'"
                  f"in inventory: {name == recherche}")


process(sys.argv[1:])
