a={'A':90, 'B':80}
print(a.get('C',70))
print(a)

if a.get('C') == None:
    a['C'] =70
print(a['C'])
print(a)


