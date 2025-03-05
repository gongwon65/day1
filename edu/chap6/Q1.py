def gugu(num):
    for x in range(10):
        print(f'{num} x {x} = {num*x}')
#gugu(3)



result = 0
for x in range(1000):
   if x % 3 or 5 == 0:
        result += x
#print(result)



def get_total_page(m,n):
    if m % n == 0:
        return m//n
    return m//n +1
#print(get_total_page(30,10))
        
'''
import sys
append = sys.argv[1]

if append == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a', encoding='utf8')
    f.write(memo)
    f.write('\n')
    f.close()
if append == '-r':
    f = open('memo.txt', 'r', encoding='utf8')
    memo=f.read()
    f.close()
    print(memo)
'''   



