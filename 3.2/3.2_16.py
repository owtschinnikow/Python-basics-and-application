"""
Sample Input:
0
10010
00101
01001
Not a number
1 1
0 0

Sample Output:
0
10010
01001
"""

import sys
import re



for line in sys.stdin:
    line = line.rstrip()
    pattern = r'(\w)\1+'
    result = re.search(pattern, line)
    if result != None:
        print(re.sub(pattern, r"\1", line))
    else:
        print(line)
