"""
Sample Input:
9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b

Sample Output:
global
None
bar
foo

create <namespace> <parent>
add <namespace> <var>
get <namespace> <var>
ключ - имя_пространства (parent),  значение - [переменные*, имена_пространств(children)]
"""
"""
namespace_dict -  {'foo': [['a'], ['global']], 'bar': [['c'], ['foo']], 'global': [['a'], []]}
"""

def return_namespace(namespace_dict, namespace, argument):
    """
    :param namespace_dict:
    :param namespace:
    :param argument:
    :return:

    >>> return_namespace({'global': [['a'], []], 'foo': [['b'], ['global']]}, 'foo', 'a')
    global

    >>> return_namespace({'global': [['a'], []], 'foo': [['b'], ['global']]}, 'foo', 'c')
    IndexError: list index out of range
    """
    if namespace not in namespace_dict:
        return print(None)
    if argument in namespace_dict[namespace][0]:
        return print(namespace)
    if not namespace_dict[namespace][1]:
        return print(None)
    return_namespace(namespace_dict, namespace_dict[namespace][1][0], argument)


def main():
    namespace_dict = {}
    number = int(input())
    for i in range(number):
        command, namespace, argument = input().split()

        if command == 'create':
            # print('create - ', namespace, argument)
            if namespace not in namespace_dict:
                namespace_dict[namespace] = [[], [argument]]
            else:
                namespace_dict[namespace][1].append(argument)
            # print('namespace_dict - ', namespace_dict)

        elif command == 'add':
            # print('add - ', namespace, argument)
            if namespace not in namespace_dict:
                namespace_dict[namespace] = [[argument], []]
            else:
                namespace_dict[namespace][0].append(argument)
            # print('namespace_dict - ', namespace_dict)

        elif command == 'get':
            # print('namespace_dict - ', namespace_dict)
            # print('get - ', namespace, argument)
            return_namespace(namespace_dict, namespace, argument)



if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    main()
