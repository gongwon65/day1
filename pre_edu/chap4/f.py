def show_price(customer):  #customer가 전달값 ,로 구분해 여러개 사용가능
    print(f'{customer} 고객님') #전달값은 함수 내에서만 사용된다.
    print('커트 가격은 10,000원 입니다.')

cus1='나장발'
#show_price(cus1)



#반환값: 함수 내 결과값을 리턴
def get_price(is_vip):
    if is_vip == True:
        return 10000
    else:
        return 15000
price = get_price(True)  #True로 정의했기에 다른 모든 입력값은 15000으로 뜸
print(f'커트 가격은{price}원입니다.')



#기본값
#def get_price(is_vip=False):
#이때 price = get_price() 인자를 넣지 않았음에도 기본값에 의해 적용됨.
#이렇게 하면 일반손님의 경우 아무것도 넣지 않아도 출력 가능


#키워드값
'''
def get_price(is_vip=False,
is_birthday=False,
is_membership=False,
card=False,
review=False,
first_time=False):
price = get_price(review=True)
#그냥 review라 하면 순서에 따라 is_vip에 review가 적용돼 vip가 true가 됨
price = get_price(review=True,is_birthday=True) #순서 무관
**41번 문제 잘 보기** p.981
'''


#가변인자 출력값 앞에 *을 입력하여 변할 수 있음을 정의의
def visit(today, *customers):
    print(today)
    for customer in customers:
        print(customer)
# **은 딕셔너리 전용
#def print_kwargs(**kwargs):
#   print(kwargs)
#print_kwargs(name='food', num=123) 하면 딕셔너리로 나온다다


'''
함수를 사용할 때 그 함수만이면 상관없는데 
함수를 통해 얻은 값을 사용해서 뭔가를 하고싶다면 return을 써야한다.
'''





#지역변수
def secret():
    message = '???'
#print(message)를 해도 message가 정의되지 않았다고 함.
#함수 내에서 print를 한다면 적용됨.


#전역변수
#함수 밖에서 선언된 변수를 함수 내에서 사용하기 위해서는
                             #global로 그 변수를 끌어온다
x = 3
def add():
    global x
    x += 3
add()
print(x)


#사용자입력
'''
num = int(input('몇분이세요'))
if num > 4:
    print('죄송하지만저희식당은최대4분까지만예약가능합니다')
'''

#파일 입출력
'''
< 열기모드>
r : read (읽기)
w : write (쓰기)
a : append (이어서쓰기)
'''
'''
f = open('list.txt', 'w', encoding='utf8') #encoding을 쓰지 않으면 한글이 깨짐짐
f.write('김xx\n') 
f.write('정xx\n') 
f.write('허xx\n')
f.close()

f = open('list.txt','r',encoding='utf8')
contents=f.read()
print(contents)
f.close()

f = open('list.txt','r', encoding='utf8')
for line in f:
    print(line, end='') # end=''을 넣지 않으면 한줄한줄 끊어서 읽음음
f.close()
'''

#with 블록을 벗어나면 자동으로 파일 닫음
with open('list.txt', 'a', encoding='utf8') as f: #f가 아니어도됨됨
    f.write('김xx\n')
    f.write('정xx\n')
    f.write('허xx\n')

f = open('list.txt', 'r', encoding='utf8')
contents = f.read()
print(contents)


#.readline()은 한줄씩 읽는 것
#.readlines()는 모든 줄을 읽고 각 줄을 요소로 가지는 리스트를 리턴





import sys

args = sys.argv[1:]
#시스템 명령어를 1번부터 읽어서 args에 적용한다
for i in args:
    print(i)
#터미널에 PS C:\gongwon> python .\chap4.\f.py 1 2 3 4
#을 치면 1 2 3 4가 줄바꿈해서 나옴



#lambda 리턴이 없는 함수 def보다 간결하고 def를 사용하지 못하는 곳에 사용
'''
add = lambda a, b:a+b
result = add(3,4)
print(result)
'''

