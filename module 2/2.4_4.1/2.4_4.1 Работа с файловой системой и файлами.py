s = []
with open('dataset_24465_4.txt') as file:
    for n, line in enumerate(file):
        s.append(line[:-1:])
    #     print(n, line[:-1:])
    # print(len(s))
    # for n, i in enumerate(s):
    #     print(n, i)

s = s[::-1]
for n, i in enumerate(s):
    print(i)



# with open('dataset_revers.txt', 'w') as revers:
#     for m, i in enumerate(s):
#         s_pop = s.pop() + '\n'
#         print(m, s_pop, end='')
#         revers.write(s_pop)


lines = open("input.txt").readlines()
with open("output.txt", "w") as out:
    out.writelines(reversed(lines))