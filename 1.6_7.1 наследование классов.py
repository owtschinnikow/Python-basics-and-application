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

"""
    if namespace not in namespace_dict:
        return print(None)
    if argument in namespace_dict[namespace][0]:
        return print(namespace)
    if not namespace_dict[namespace][1]:
        return print(None)
    return_namespace(namespace_dict, namespace_dict[namespace][1][0], argument)
"""



def check_class(namespace_dict, namespace_parent, namespace_child):
    if namespace_parent not in namespace_dict:
        return 'No'
    if namespace_parent == namespace_child:
        return 'Yes'
    if namespace_parent in namespace_dict[namespace_child]:
        return 'Yes'
    # if namespace_child in namespace_dict[namespace_parent]:
    #     return print('No')
    for namespace in namespace_dict[namespace_child]:
        # print('ANSWER - namespace_dict[namespace_child]', namespace_dict[namespace_child])
        check_class(namespace_dict, namespace_parent, namespace)


def main():
    namespace_dict = {}
    number = int(input())
    for i in range(number):
        data_input = input()
        # print(data_input)
        if ' : ' not in data_input:
            namespace_dict[data_input] = []
        else:
            namespace_parent, namespace_child = data_input.split(' : ')
            namespace_dict[namespace_parent] = [*namespace_child.split()]

    print(namespace_dict)

    quantity = int(input())
    for i in range(quantity):
        namespace_parent, namespace_child = input().split()
        print('REQUEST - ', namespace_parent, namespace_child)
        # check_class(namespace_dict, namespace_parent, namespace_child)
        print(check_class(namespace_dict, namespace_parent, namespace_child))


if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    main()
