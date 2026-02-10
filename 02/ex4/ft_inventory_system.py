import sys


def find(diction: dict, recherche: str) -> bool:

    """this function to find i word in a dictionary"""

    if not diction or not str:
        return False
    for name in diction:
        if name == recherche:
            return True
    return False


def process(args: list) -> None:

    """ this function take args in forme of key: value
    then i parce them into dictionary of item: quantity
    this is the base  dictionary ill use to perfome my analytics"""

    if not args:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <key(name):value(quantite)> ...")
        return
    dictio = {}
    total_items = 0
    total_keys = 0
    grouped = {"abundant": {}, "moderate": {}, "scarce": {}}

    for arg in args:
        try:
            key, value = arg.split(":")
            dictio[key] = int(value)
        except Exception as e:
            print(e)
            print("error : check the patern/validation of inputs")
            return

    for name, quantity in dictio.items():
        if quantity == 1:
            grouped["scarce"][name] = quantity
        elif quantity == 2:
            grouped["moderate"][name] = quantity
        else:
            grouped["abundant"][name] = quantity

    for y in dictio.values():
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
    for key, value in dictio.items():
        if value == least:
            print(f"Least abundant: {key} ({value} units)")
            break

    print("\n=== Item Categories ===")
    catego = {"Moderate": {}, "Scarce": {}}
    for name, value in dictio.items():
        if value >= 5:
            catego["Moderate"][name] = value
        else:
            catego["Scarce"][name] = value
    print(f"Moderate: {catego.get('Moderate')}")
    print(f"Scarce: {catego.get('Scarce')}\n")

    print("=== Management Suggestions ===")
    print(f"Restock needed: {list(grouped['scarce'].keys())}")
    grouped.update(catego)
    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(dictio)}")
    print(f"Dictionary values: {list(dictio.values())}")
    recherche = "sword"
    print(f"Sample lookup - '{recherche}'"
          f"in inventory: {find(dictio, recherche)}")


if __name__ == '__main__':
    process(sys.argv[1:])
