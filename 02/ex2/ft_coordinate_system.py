import sys
import math


class BadCoordinate(Exception):
    """Raise when coordinate can't be parsed into int"""
    pass


def all_is_int(splited: list) -> bool:
    for splt in splited:
        try:
            int(splt)
        except ValueError:
            return False
    return True


def invalide_parse(lst: list) -> None:
    for elem in lst:
        try:
            int(elem)
        except ValueError as e:
            raise BadCoordinate("Error parsing coordinates:", e)


def parsing(strr: str) -> tuple | None:
    tpl = strr.split(",")
    if len(tpl) != 3:
        print("invalid format")
        return None
    elif not all_is_int(tpl):
        print(f"Parsing invalid coordinates: \"{strr}\"")
        try:
            invalide_parse(tpl)
        except BadCoordinate as e:
            a, b = e.args
            print(a, b)
            print(f"Error details - Type: ValueError, Args: (\"{b})\",)")
        return None
    else:
        print(f"Parsing coordinates: \"{strr}\"")
        try:
            tpl = tuple(int(arg) for arg in tpl)
        except ValueError:
            print("invalid literal for int() with base 10 and")
            return None
        return tpl


def process(args: list) -> None:
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
    dist = math.sqrt((tpl[0]-point_o[0])**2 +
                     (tpl[1]-point_o[1])**2 +
                     (tpl[2]-point_o[2])**2)
    print(f"{dist:.2f}\n")

    print("Unpacking demonstration:")
    try:
        x, y, z = tpl
    except Exception as e:
        print(e)
        return
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y} ,Z={z}")


if __name__ == '__main__':
    process(sys.argv[1:])
