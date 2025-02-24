print('안녕하세요'*2)

'''
num = input('숫자를 입력하세요: ')
print(10 + int(num))
'''



'''
num = input('숫자를 입력하세요: ')
if int(num2) == 0:
    print('짝수')
else:
    print('홀수')
'''


'''
num = input('숫자를 입력하세요: ')
plus = int(num) + 20
if plus <= 255:
    print(plus)
else:
    print(255)
'''
    

'''
num = input('숫자를 입력하세요: ')
plus = int(num) - 20
if plus < 0:
    print(0)
elif plus > 255:
    print(255)   
else:
    print(plus)
'''


'''
user = input('현재시간:')
if user[-2:] == '00':
    print('정각 입니다.')
else:
    print('정각이 아닙니다.')
'''




'''
fruit = ["사과", "포도", "홍시"]
user = input('좋아하는 과일은? ')
if user in fruit:
    print('정답입니다.')
else:
    print('정답이 아닙니다.')
'''

    
    
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input('좋아하는 계절은? ')
if user in fruit.keys():
    print('correct')
else:
    print('incorrect')

















    
    