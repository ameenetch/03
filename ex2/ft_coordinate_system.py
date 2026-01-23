import sys
import math


def all_is_int(splited: list) -> bool:
    for splt in splited:
        try:
            int(splt)
        except ValueError:
            return False
    return True


def invalide_parse(lst: list):
    for elem in lst:
        try:
            int(elem)
        except ValueError:
            print(f"Error parsing coordinates: "
                  f"invalid literal for int() with base 10: '{elem}'")
            print(f"Error details - Type: ValueError, Args: "
                  f"(\"invalid literal for int() with base 10: '{elem}'\",)\n")


def parsing(strr: str) -> tuple | None:
    tpl = strr.split(",")
    if len(tpl) != 3:
        print("invalid format")
        return None
    elif not all_is_int(tpl):
        print(f"Parsing invalid coordinates: \"{strr}\"")
        invalide_parse(tpl)
        return None
    else:
        print(f"Parsing coordinates: \"{strr}\"")
        try:
            tpl = tuple(int(arg) for arg in tpl)
        except ValueError:
            print("invalid literal for int() with base 10 and")
            return None
        return tpl


def process(args: list):
    point_o = (0, 0, 0)
    if len(args) != 3 and len(args) != 1:
        print("invalide format")
        return

    elif len(args) == 3:
        try:
            tpl = tuple(int(arg) for arg in args)
        except ValueError:
            print("invalid literal for int() with base 10 and")
            return

        print(f"Position created: {tpl}")

    elif len(args) == 1:
        tpl = parsing(args[0])
        if not tpl:
            return
        print(f"Parsed position: {tpl}")

    print(f"Distance between {point_o} and {tpl}: ", end=" ")
    print(f"{math.sqrt((tpl[0] - point_o[0])**2 +
                       (tpl[1] - point_o[1])**2 +
                       (tpl[2] - point_o[2])**2):.2f}\n")

    print("Unpacking demonstration:")
    x, y, z = tpl
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y} ,Z={z}")


process(sys.argv[1:])
