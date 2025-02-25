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

'''
import sys

def calculate(num1, num2, operator):
    # 연산 기호에 따른 계산
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operator. Please use +, -, *, or /."

# 명령 줄 인수가 정확히 3개인지 확인 (연산자, 두 숫자 포함)
if len(sys.argv) != 4:
    print("사용법: python 프로그램명.py <숫자1> <숫자2> <연산자>")
else:
    # 명령 줄 인수에서 숫자와 연산자를 추출
    try:
        num1 = float(sys.argv[1])  # 첫 번째 숫자
        num2 = float(sys.argv[2])  # 두 번째 숫자
        operator = sys.argv[3]     # 연산자
    except ValueError:
        print("Error: 입력값은 숫자여야 합니다.")
        sys.exit(1)
    
    # 계산 결과 출력
    result = calculate(num1, num2, operator)
    print(f"결과: {result}")
'''