import sys

# def gen(max):
#     count = []
#     i = 0
#     while i < max:
#         count.append(i)
#         i += 1
#     return count


# nbrs = gen(10)
# print(nbrs)
# for i in nbrs:
#     print(i)

# print(sys.getsizeof(gen))
# print(sys.getsizeof(nbrs))


# def gen2(max):
#     i = 0
#     while i < max:
#         yield i
#         i += 1


# c = gen2(10)
# for i in c:
#     print(i)


def fibo(n):
    print("start gen")
    yield 0
    x = 1
    y = 0
    i = 0
    while i < n:
        yield x
        x += y
        y = x - y
        i += 1
    print("end gen")


s = fibo(4)
# print(s)
# print(type(s))
for i in s:
    print("enter the loop")
    print(i)
    print("finish the loop")


# print(sys.getsizeof(fibo))

