"""
Sample Input:
zabcz
zzz
zzxzz
zz
zxz
zzxzxxz

Sample Output:
zabcz
zzxzz
"""

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'.*z...z.*'
    result = re.search(pattern, line)
    if result != None:
        print(line)
