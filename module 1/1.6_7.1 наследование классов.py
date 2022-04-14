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

"""
    'A G',      # Yes   # A предок G через B/C, D, F
    'A Z',      # No    # Y потомок A, но не Y
    'A W',      # Yes   # A предок W через Y, V
    'X W',      # Yes   # X предок W через Y, V
    'X QWE',    # No    # нет такого класса QWE
    'A X',      # No    # классы есть, но они нет родства :)
    'X X',      # Yes   # родитель он же потомок
    '1 1',      # No    # несуществующий класс
"""


import collections

def breadth_first_search(graph, root, peak):
    if root not in graph:
        return print('No')
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    # print(peak, root, visited, end=' ')
    if peak in visited:
        print('Yes')
    else:
        print('No')

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

    # print(namespace_dict)

    quantity = int(input())
    for i in range(quantity):
        namespace_parent, namespace_child = input().split()
        breadth_first_search(namespace_dict, namespace_child, namespace_parent)




if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    main()
