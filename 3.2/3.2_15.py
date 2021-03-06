"""
Буквой считается символ из группы \w.

Sample Input:
attraction
buzzzz
mewmewNnyaaa

Sample Output:
atraction
buz
mewmewNnya

https://regex101.com/#python
"""

import sys
import re


for line in sys.stdin:
    line = line.rstrip()
    pattern = r'(\w)\1+'
    print(re.sub(pattern, r"\1", line))

