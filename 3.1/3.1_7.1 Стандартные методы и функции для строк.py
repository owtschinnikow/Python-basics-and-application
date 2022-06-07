"""
Sample Input 1:
abababa
aba
Sample Output 1:
3

Sample Input 2:
abababa
abc
Sample Output 2:
0

Sample Input 3:
abc
abc
Sample Output 3:
1

Sample Input 4:
aaaaa
a
Sample Output 4:
5
"""


def number_of_occurrences(s, t):
    ans = 0
    while t in s:
        start = s.find(t) + 1
        s = s[start:]
        ans += 1
    return ans


def main():
    s, t = input().upper(), input().upper()
    print(number_of_occurrences(s, t))


def test():
    lst = [
        ['abababa', 'aba', 3],
        ['abababa', 'abc', 0],
        ['abc', 'abc', 1],
        ['aaaaa', 'a', 5],
        ['cvcabacvcaba', 'aba', 2],
    ]
    n = len(lst)
    for i, el in enumerate(lst):
        answer = number_of_occurrences(el[0], el[1])
        if answer == el[2]:
            print(f'{i + 1} of {n} is OK', 'answer = ', answer)
        else:
            print(f'{i + 1} of {n} is Fail', 'answer = ', answer, el[2])


if __name__ == '__main__':
    test()
    # main()
