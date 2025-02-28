


import re

text = 'hello, elice!'

p1 = 'elice'

m1 = re.findall(p1, text)

print(m1)




p = re.compile('[a-z]+')
result = p.finditer("life is too short")
print(result)
for r in result:
    print(r)
