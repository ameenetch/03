import sys


def print_commande(args: list) -> None:
    if not args:
        return
    print("=== Command Quest ===")
    if len(args) == 1:
        print("No arguments provided!")
        print(f"Program name: {args[0]}")
        print(f"Total arguments: {len(args)}")

    elif len(args) > 1:
        print(f"Program name: {args[0]}")
        print(f"Arguments received: {len(args) - 1}")
        x = 1
        while x < len(args):
            print(f"Argument {x}: {args[x]}")
            x += 1
        print(f"Total arguments: {len(args)}")


if __name__ == '__main__':
    print_commande(sys.argv)
