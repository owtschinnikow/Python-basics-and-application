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
    return visited


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
    namespace_parent_list = []
    namespace_parent_list_wrong = []
    for i in range(quantity):
        namespace_parent_list.append(input())
    # print(namespace_parent_list, '\n')

    for n, namespace in enumerate(namespace_parent_list):
        # print(n, namespace)
        if namespace in namespace_parent_list[0:n]:
            # print(namespace, namespace_parent_list[0:n])
            print(namespace)
            # print()
            namespace_parent_list_wrong.append(namespace)

        else:
            breadth_first_search_list = breadth_first_search(namespace_dict, namespace)
            # print(namespace, namespace_parent_list[0:n], breadth_first_search_list)
            for i in breadth_first_search_list:
                if i in namespace_parent_list[0:n]:
                    print(namespace)
                    break
            # print()



if __name__ == '__main__':
    main()
