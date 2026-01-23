import sys

dict = {}
for arg in sys.argv[1:]:
    x, y = arg.split(":")
    dict[x] = y

print(dict)

x = "hello world how are you"
print(x.split())

print(dict)
