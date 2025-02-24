#1

def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
number = is_odd(2)
if number is True:
    print('홀수')
else:
    print('짝수')


#2
'''
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)
    print(avg_numbers)
print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))
'''

#3
'''
input1 = input('첫 번째 숫자를 입력하세요:')
input2 = input('두 번째 숫자를 입력하세요:')

total = int(input1) + int(input2)
print('두 수의 합은 %s입니다.' % total)
''' #int말고 다시해봐

#4
'''
3번만 띄어쓰기기
print('you','need','python')
'''


#5
'''
with open("test.txt", 'w',encoding='utf8') as f1:
    f1.write("Life is too short")

with open("test.txt", 'r',encoding='utf8') as f2:
    print(f2.read())
'''


#6
'''
user_input = input("저장할 내용을 입력하세요 : ")
with open('test.txt','a',encoding='utf8') as f:
    f.write(user_input)
    f.write('\n')
'''


#7
'''
f = open('test.txt', 'r',encoding='utf8')
body = f.read()
f.close()

body = body.replace('java','python')
f = open('test.txt', 'w',encoding='utf8')
f.write(body)
f.close()
'''