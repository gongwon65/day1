#Q6
import sys

def basic(num1,num2,operation):
    if operation == '*':
        print(num1*num2)
    elif operation == '/':
        if num2 == 0:
          print('0으로 나눌 수 없습니다.') 
        else:
            print(num1/num2)
    elif operation == '+':
        print(num1+num2)
    elif operation == '-':
        print(num1-num2)
    else:
        print('사칙연산 기호를 제대로 입력해주십시오')


num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
operation = sys.argv[3]
    
basic(num1,num2,operation)
