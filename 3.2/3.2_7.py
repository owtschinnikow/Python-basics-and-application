"""
Sample Input:
catcat
cat and cat
catac
cat
ccaatt

Sample Output:
catcat
cat and cat
  cat    cat
"""

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'[\S\s\w]*cat[\S\s\w]*cat[\S\s\w]*'
    if re.search(pattern, line) != None:
        match_object = re.search(pattern, line)
        print(line)
        # print(match_object.group(0))
    else:
        pass