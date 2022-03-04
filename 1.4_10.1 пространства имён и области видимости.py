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

cmd, namesp, arg = input().split()
