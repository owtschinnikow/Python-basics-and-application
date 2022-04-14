"""
Sample Input:
4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError

Sample Output:
FileNotFoundError
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
    quantity = int(input())
    for i in range(quantity):
        namespace_parent, namespace_child = input().split()
        breadth_first_search(namespace_dict, namespace_child, namespace_parent)

if __name__ == '__main__':
    main()