import sys


def process(args: list) -> None:
    if not args:
        return
    print("=== Player Score Analytics ===")
    if len(args) == 1:
        print("No scores provided. Usage:"
              " python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        x = 1
        list = []
        while x < len(args):
            try:
                list += [int(args[x])]
            except ValueError:
                print(f"oops, I typed {args[x]} instead of a valid Number")
                return
            except Exception:
                print("oops, Someting went wrong")
                return
            x += 1
        print(f"Scores processed: {list}")
        print(f"Total players: {len(list)}")
        print(f"Total score: {sum(list)}")
        print(f"Average score: {sum(list)/len(list):.1f}")
        print(f"High score: {max(list)}")
        print(f"Low score: {min(list)}")
        print(f"Score range: {max(list) - min(list)}\n")


process(sys.argv)
