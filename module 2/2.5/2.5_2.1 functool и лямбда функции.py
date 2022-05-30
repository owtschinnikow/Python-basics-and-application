x = input().split()
print(x)
xs = (int(i) for i in x)
print(xs)

def even(x):
    return False

events = filter(even, xs)
print(events)
for i in events:
    print(i)