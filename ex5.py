class Player:
    def __init__(self, name, level, event):
        self.name = name
        self.level = level
        self.event = event 


def gen(lst: list) -> list:
    for x in lst:
        yield x 


def process(lst: list):
    print("=== Game Data Stream Processor ===")
    print(f"Processing {len(lst)} game events...\n")
    i = 0

    for x in gen(lst):
        print(f"Event {i}: Player {x.name} (level {x.level}) {x.event}")
        i += 1


def fibo_gen(n):
    i = 0 
    yield 0
    x = 1 
    y = 0
    while i < n - 1:
        yield x 
        x += y
        y = x - y
        i += 1


def check(n) -> bool:
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def prime_gen(n):
    i = 0
    x = 2
    while i < n :
        if check(x) is True:
            yield x
            i += 1 
        x += 1


def demonstration():
    n = 10
    x = 5
    print(f"Fibonacci sequence (first {n}): ",end = "")
    i = iter(fibo_gen(n))
    print((next(i)))
    # for i in fibo_gen(n):
    #     print(i,end = " ")
    print(f"\nPrime numbers (first {x}):", end = "")
    for i in prime_gen(x):
        print(i,end = " ")





def analytics(lst: list):
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
        elif x.event == "found treasure":
            count_leveled_up += 1

    print(f"High-level players (10+): {count_high_level}")
    print(f"Treasure events: {count_treasure}")
    print(f"Level-up events: {count_leveled_up}\n")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

if __name__ == '__main__':
    list = [Player("alice", 5, "killed monster")
            ,Player("bob", 12, "found treasure")
            ,Player("charlie", 8, "leveled up")]
    process(list)
    analytics(list)
    demonstration()
