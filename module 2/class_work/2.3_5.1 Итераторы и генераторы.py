import itertools
import math

def primes():
    a = 1
    while True:  # просто пример
        a += 1
        if (math.factorial(a - 1) + 1) % a  == 0:
            yield a

print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


