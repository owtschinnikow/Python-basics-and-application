"""
Sample Input 1:
ababa
a
b
Sample Output 1:
1

Sample Input 2:
ababa
b
a
Sample Output 2:
1

Sample Input 3:
ababa
c
c
Sample Output 3:
0

Sample Input 4:
ababac
c
c
Sample Output 4:
Impossible

Если а присутствует в b и а присутствует в s - угадайте, что будет?
"""


def count_replaces(s, a, b):
    n = 0
    if a not in s:
        return n
    elif a in b:
        return 'Impossible'
    while n < 1000:
        control_number = 0
        while control_number != -1:
            s = s[:control_number] + b + s[control_number + len(a):]
            control_number = s[control_number + len(b):].find(a) + len(b) + control_number
            # print(control_number, s)
        else:
            break
        n += 1
    if n < 1000:
        return n
    else:
        return 'Impossible-1'


def main():
    s, a, b = input().upper(), input().upper(), input().upper()
    print(count_replaces(s, a, b))


def test():
    lst = [
        ["ababa", "a", "b", 1],  # замены конечны
        ["ababa", "b", "a", 1],  # замены конечны
        ["ababa", "c", "c", 0],  # замен не будет
        ["ababac", "c", "c", "Impossible"],  # меняем строку на самоё себя
        ["ccacc", "cac", 'caca', "Impossible"],  # замены бесконечны
        ["ccacc", "cac", 'accca', "Impossible"],  # замены бесконечны и экспоненциально увеличивают строку
        ["abababa", "aba", 'ada', 2]
    ]
    n = len(lst)
    for i, el in enumerate(lst):
        answer = count_replaces(el[0], el[1], el[2])
        if answer == el[3]:
            print(f"{i + 1} of {n} is OK", 'answer = ', answer)
        else:
            print(f"{i + 1} of {n} is Fail", 'answer = ', answer)


if __name__ == '__main__':
    test()
    # main()
