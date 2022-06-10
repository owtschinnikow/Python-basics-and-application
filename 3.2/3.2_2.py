import re

# print(re.match)
# print(re.search)
# print(re.findall)
# print(re.sub)

pattern = r'abc'
string = 'abc'
# match_object = re.match(pattern, string)
print(re.match(pattern, string))
print(re.search(pattern, string))
print(re.findall(pattern, string))
print(re.sub(pattern, string))