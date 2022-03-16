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
    namespace_dict = {}
    number = int(input())
    for i in range(number):
        data_input = input()
        if len(data_input) == 1:
            print(data_input)
            namespace_dict[data_input] = []
        else:
            namespace_parent, namespace_child = data_input.split(' : ')
            print(namespace_parent, *namespace_child.split())
            namespace_dict[namespace_parent] = [*namespace_child.split()]

    print(namespace_dict)

    quantity = int(input())
    for i in range(quantity):
        namespace_parent, namespace_child = input().split()
        print(namespace_parent, namespace_child)
        if namespace_parent


if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    main()
