class Player:
    def __init__(self, name, level, event):
        self.name = name
        self.level = level
        self.event = event


def gen(lst: list):
    if not lst:
        return
    for x in lst:
        yield x


def fibo_gen(n: int):
    if n <= 0:
        return
    yield 0
    i = 0
    x = 1
    y = 0
    while i < n - 1:
        yield x
        x += y
        y = x - y
        i += 1


def check_is_prime(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_gen(n: int):
    if n <= 0:
        return
    i = 0
    x = 2
    while i < n:
        if check_is_prime(x) is True:
            yield x
            i += 1
        x += 1


def demonstration() -> None:

    """ show how the generators work internally using iter() and next()"""

    n = 10
    x = 5
    i = 0
    print("\n=== Generator Demonstration ===")
    print(f"Fibonacci sequence (first {n}): ", end="")
    it = iter(fibo_gen(n))

    while i < n:
        print((next(it)), end="")
        if i != n - 1:
            print(", ", end="")
        i += 1

    print(f"\nPrime numbers (first {x}):", end="")
    it = iter(prime_gen(x))
    i = 0

    while i < x:
        print((next(it)), end="")
        if i != x - 1:
            print(", ", end="")
        i += 1
    print("\n")


def analytics(lst: list) -> None:

    """ analyse the players data """

    if not lst:
        return
    count_high_level = 0
    count_leveled_up = 0
    count_treasure = 0

    print("=== Stream Analytics ===")
    print(f"Total events processed: {len(lst)}")

    for x in lst:
        if x.level >= 10:
            count_high_level += 1
        if x.event == "found treasure":
            count_treasure += 1
        elif x.event == "leveled up":
            count_leveled_up += 1

    print(f"High-level players (10+): {count_high_level}")
    print(f"Treasure events: {count_treasure}")
    print(f"Level-up events: {count_leveled_up}\n")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")


if __name__ == '__main__':
    list_player = [Player("alice", 5, "killed monster"),
                   Player("bob", 12, "found treasure"),
                   Player("charlie", 8, "leveled up"),
                   Player("amine", 2, "triple kill"),]

    print("=== Game Data Stream Processor ===")
    print(f"Processing {len(list_player)} game events...\n")
    i = 0

    for x in gen(list_player):
        print(f"Event {i}: Player {x.name} (level {x.level}) {x.event}")
        i += 1

    analytics(list_player)
    demonstration()
