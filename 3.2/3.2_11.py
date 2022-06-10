"""
Sample Input:
blabla is a tandem repetition
123123 is good too
go go
aaa

Sample Output:
blabla is a tandem repetition
123123 is good too

https://regex101.com/#python
"""

import sys
import re


for line in sys.stdin:
    line = line.rstrip()
    pattern = r'\b(\w*)\1\b'
    result = re.search(pattern, line)
    if result != None:
        print(line)
