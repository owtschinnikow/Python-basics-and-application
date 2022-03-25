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

"Yes", если класс 1 является предком класса 2
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
    """
    Класс A является предком класса B, если
    A = B;
    A - прямой предок B
    существует такой класс C, что C - прямой предок B и A - предок C

    :param namespace_dict:
    :param namespace_parent:
    :param namespace_child:
    :return:
    """
    if namespace_parent == namespace_child:
        return 'Yes'
    if namespace_parent in namespace_dict[namespace_child]:
        return 'Yes'
    # if namespace_child not in namespace_dict:
    #     return 'No'
    for namespace in namespace_dict[namespace_child]:
        check_class(namespace_dict, namespace_parent, namespace)


def main():
    namespace_dict = {}
    number = int(input())
    for i in range(number):
        data_input = input()
        if ' : ' not in data_input:
            namespace_dict[data_input] = []
        else:
            namespace_child, namespace_parent  = data_input.split(' : ')
            namespace_dict[namespace_child] = [*namespace_parent.split()]

    print(namespace_dict)

    quantity = int(input())
    for i in range(quantity):
        namespace_parent, namespace_child = input().split()
        answer = check_class(namespace_dict, namespace_parent, namespace_child)
        print(namespace_parent, namespace_child, answer)

if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    main()
