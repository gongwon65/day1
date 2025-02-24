#1
a=80
b=75
c=55
print((a+b+c)/3)

#2?
num = 13
if num % 2 == 0:
    print('짝수')
else:
    print('홀수')

#3
reg='881120-1068234'
print(reg[:6])
print(reg[7:])
#print(reg.split('-'))

#4
print(reg[7])

#5
e='a:b:c:d:'
new_e=e.replace(':','#')
print(new_e)

#6
Q6=[1,3,5,4,2]
Q6.sort()
Q6.reverse()
print(Q6)

#7
str=['Life','is','too','short']
print(' '.join(str))

#8
Q8=(1,2,3)
Q8_2=(4,)
print(Q8+Q8_2)

#9
f=dict()
f['name']='python'
print(f)

f[('f',)]='python'
print(f)

#f[[1]]='python'

f[250]='python'
print(f)

#10
g = {'A':90, 'B':80, 'C':70}
print(g['B'])

#11
h = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
set_h = set(h)
list_h = list(set_h)
print(list_h)

#12
i = j = [1, 2, 3]
i[1] = 4
print(j)
print(id(i),id(j)) #i와 j에 할당된 공간이 같음
