
try:
    x = [1, 2, "hello", 7]
    x.sort()
    print(x)
except TypeError:
    print("TypeError")

print("I can catch")