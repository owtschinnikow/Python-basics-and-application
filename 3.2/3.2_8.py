"""
Sample Input:
cat
catapult and cat
catcat
concat
Cat
"cat"
!cat?

Sample Output:
cat
catapult and cat
"cat"
!cat?
"""

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'\bcat\b'
    result = re.search(pattern, line)
    if result != None:
        print(line)

