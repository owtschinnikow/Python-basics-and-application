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

def breadth_first_search(graph, root):
    visited, queue = [], collections.deque([root])
    visited.append(root)
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    print(visited)
    # print(*list(visited))
    # if len(visited) != 1:
    #     if list(visited)[0] !=

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
    namespace_parent_space = []
    for i in range(quantity):
        namespace_parent = input()
        namespace_parent_space.append(namespace_parent)
        # print(namespace_parent)
        print(namespace_parent_space)
        breadth_first_search(namespace_dict, namespace_parent)


if __name__ == '__main__':
    main()
