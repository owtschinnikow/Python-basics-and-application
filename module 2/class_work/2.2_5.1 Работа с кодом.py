"""
Sample Input 1:
2016 4 20
14
Sample Output 1:
2016 5 4

Sample Input 2:
2016 2 20
9
Sample Output 2:
2016 2 29

Sample Input 3:
2015 12 31
1
Sample Output 3:
2016 1 1
"""

import datetime

year, month, day = map(int, input().split())
day_delta = int(input())
date_old = datetime.date(year, month, day)

delta = datetime.timedelta(day_delta)

date_new = date_old + delta

print(date_new.year, date_new.month, date_new.day)