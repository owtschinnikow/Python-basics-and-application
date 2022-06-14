"""
Буквой считается символ из группы \w.

Sample Input:
attraction
buzzzz

Sample Output:
atraction
buz

https://regex101.com/#python
"""

import sys
import re


for line in sys.stdin:
    line = line.rstrip()
    pattern = r'\b(\w)(\w)'
    result = re.search(pattern, line)
    if result != None:
        print(re.sub(pattern, r"\2\1", line, count=0, flags=re.IGNORECASE))
