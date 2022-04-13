def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res

print(s(5, 5, 5, 5, 1))
print(s(11, 10, b=10))
print(s(21))
print(s(b=31))

s(5, 5, 5, 5, 1)

s(11, 10, b=10)
s(21)
s(11, b=20)

s(11, 10)