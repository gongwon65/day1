a = input('더할숫자: ')
b = a.split(',')
c = map(int,b)

'''
result=(sum(c))
print(result)
'''

result=0
for i in c:
    result += i
print(result)
