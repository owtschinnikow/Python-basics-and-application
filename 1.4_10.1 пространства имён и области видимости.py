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
"""

command_list = ['create', 'add', 'get']

# def read_data():
#     command, namespace, argument = input().split()
#     return command, namespace, argument

def main():
    namespace_dict = {'global': []}
    number = int(input())
    for i in range(number):
        command, namespace, argument = input().split()
        if command == command_list[0]:
            namespace_dict[argument] = [namespace]
            print(namespace_dict)
        if command == command_list[1]:
            namespace_dict[namespace].append(argument)
            print(namespace_dict)
        if command == command_list[2]:
            namespace_dict[namespace]
            print(namespace_dict)


if __name__ == '__main__':
    main()
