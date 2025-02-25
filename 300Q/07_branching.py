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

    
'''
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input('좋아하는 계절은? ')
if user in fruit.keys():
    print('correct')
else:
    print('incorrect')
'''



'''
user = input('문자를 입력하시오: ')
dis = user.islower()
if dis == True:            #굳이 True를 붙이지 않아도 됨.
    print(user.upper())
else:
    print(user.lower())
'''



'''
user = input('점수를 입력하시오: ')
score = int(user)
if score <= 20:
    print('grade is E')
elif score <= 40:
    print('grade is D')
elif score <= 60:
    print('grade is C')
elif score <= 80:
    print('grade is B')
else:
    print('grade is A')
'''




'''
user = input('환전할 금액을 입력하시오: ')
user_split = user.split(' ')
money = int(user_split[0])
typ = user_split[1]


if typ == '달러':
    print(f'{1167*money:.2f}', '원')
elif typ == '엔':
    print(f'{1.096*money:.2f}', '원')
elif typ == '유로':
    print(f'{1268*money:.2f}', '원')
else:
    print(f'{171*money:.2f}', '원')
'''
#너무 if문만 생각한다 다양하게 보자.

'''
환율 = {"달러": 1167, 
        "엔": 1.096, 
        "유로": 1268, 
        "위안": 171}
user = input("입력: ")
num, currency = user.split()
print(float(num) * 환율[currency], "원")
'''








    
    