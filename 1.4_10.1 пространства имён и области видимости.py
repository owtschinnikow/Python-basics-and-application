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
"""

def main():
    number = input().split()
    command, namespace, argument = input().split()


if __name__ == '__main__':
    main()
