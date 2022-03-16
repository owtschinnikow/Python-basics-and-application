"""
Sample Input:
4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A

Sample Output:
Yes
Yes
Yes
No
"""

def main():
    number = int(input())
    for i in range(number):
        command, namespace, argument = input().split()

        if command == 'create':
            # print('create - ', n


if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    main()
