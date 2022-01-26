ans = 0

objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]

objects_set = set()
for obj in objects:  # доступная переменная objects
    objects_set.add(id(obj))
ans = len(objects_set)

print(ans)




