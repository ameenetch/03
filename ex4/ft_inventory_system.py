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
    grouped = {"low": {}, "medium": {}, "high": {}}
    for arg in args:
        key, value = arg.split(":")
        dictio[key] = int(value)

    for name, quantity in dictio.items():
        if quantity == 1:
            grouped["low"][name] = quantity
        elif 2 <= quantity <= 3:
            grouped["medium"][name] = quantity
        else:
            grouped["high"][name] = quantity
################################################################################
    for item in grouped.items():
        
################################################################################
    analysiste(dictio)
#     least = min(dictio.values())
#     moore = max(dictio.values())

#     for key, value in dictio.items():
#         if value == moore:
#             print(f"Most abundant: {key} ({value} units)")
#             break
#     print()
#     for key, value in dictio.items():
#         if value == least:
#             print(f"Least abundant: {key} ({value} units)")
#             break
#     restock_needed(dictio)


process(sys.argv[1:])
