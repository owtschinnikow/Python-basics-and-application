"""
Примечание:
Обратите внимание на параметр count у функции sub.

Sample Input:
There’ll be no more "Aaaaaaaaaaaaaaa"
AaAaAaA AaAaAaA

Sample Output:
There’ll be no more "argh"
argh AaAaAaA
"""

import sys
import re


for line in sys.stdin:
    line = line.rstrip()
    pattern = r'([aA])+'
    result = re.search(pattern, line)
    if result != None:
        print(re.sub(pattern, 'argh', line, count=1, flags=re.IGNORECASE))

