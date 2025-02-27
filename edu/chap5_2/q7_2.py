#Q7
number = input("숫자를 입력하세요: ")
try:
    squared_number = int(number) ** 2
except:
    print('아라비아 숫자로 입력해 주십시오')
else:
    print("입력한 숫자의 제곱:", squared_number)