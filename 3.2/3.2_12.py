"""
Sample Input:
I need to understand the human mind
humanity

Sample Output:
I need to understand the computer mind
computerity
"""

import sys
import re


for line in sys.stdin:
    line = line.rstrip()
    pattern = r'human'
    result = re.search(pattern, line)
    if result != None:
        print(re.sub(pattern, 'computer', line))
    else:
        print(line)
