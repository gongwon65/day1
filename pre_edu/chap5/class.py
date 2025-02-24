'''
변수 < 함수 < 클래스
파이썬: 대화형 인터프리터
C: 절차식 언어어
C++, java, c# : 객체지향언어
'''


#class
'''
class 클래스명:
정의
class BlackBox  -> 앞글자를 대문자로
'''

'''
class BlackBox:
    pass
b1 = BlackBox() # b1 객체생성, 객체 변수수
b2 = BlackBox()

b1.name = "까망이"
print(b1.name)
print(isinstance(b1, BlackBox)) #b1은 BlackBox의 인스턴스인지 물어보는 함수
'''


# __init__ *더블 언더바가 달린 함수는 콜을 하지 않아도 조건만 맞으면 됨
#객체가 생성될 때 자동으로 작동하는 함수

class BlackBox:
    def __init__(self, name, price): #class내 함수엔 처음 self 고정값
        self.name = name 
        self.price = price
    
    #def set_travel_mode(self, min):
    #    print(f'{self.name}{min}분 동안 여행모드 On')

b1 = BlackBox('까망이', 200000)
b2 = BlackBox('하양이', 100000)
'''
print(b1.name, b1.price)
print(b2.name, b2.price)
'''
#b1.set_travel_mode(30)
#b2.set_travel_mode(10)


#상속
'''
기본블박
class BlackBox:
def __init__(self, name, price):
self.name= name
self.price= price

여행모드 블박
class TravelBlackBox:
def __init__(self, name, price):
self.name= name
self.price= price
def set_travel_mode(self, min):
print(str(min) + “분동안여행모드ON”)

즉, 이름하고 가격정의가 중복되므로 상속을 이용함
'''

'''
class TravelBlackBox(BlackBox): #BlackBox의 class를 가져다가 쓰겠다
    def set_travel_mode(self, min):
        print(str(min) + '분동안여행모드ON')

b3 = TravelBlackBox('노랭이', 300000)
b3.set_travel_mode(20)
#BlackBox 사용 시 .set_travel_mode()는 사용불가 - 자식클래스 기능이기에
'''



#다중상속
class VideoMaker:
    def make(self):
        print('추억용 여행영상 제작')

class MailSender:
    def send(self):
        print('메일발송')



#super 자식클래스에서 부모클래스를 부르는 방법
class TravelBlackBox(BlackBox,VideoMaker,MailSender):
    def __init__(self, name, price, sd):
        super().__init__(name, price)        #여기는 self가 없음
        self.sd = sd

    def set_travel_mode(self, min):
        print(str(min) + '분동안여행모드ON')

b4 = TravelBlackBox('푸릉이',500000,64)
'''
b4.set_travel_mode(30)
print(b4.sd)

b4.make()
b4.send()
'''


#메소드 오버 라이딩  -> 자식클래스에서 부모클래스의 메소드 새로 정의 가능하고 자식이 우선 호출됨

class AdvancedTravelBlackBox(TravelBlackBox): 
    def set_travel_mode(self, min):
        print(f'{self.name}{min}분동안 여행모드 On')
        self.make() # 추억용여행영상제작
        self.send() # 메일발송  

b5 = AdvancedTravelBlackBox('분홍이',10000, 72)
#b5.set_travel_mode(60)



#pass       -> 정의는 해두되 나중에 하겠다.
'''
for i in range(10):
    pass
while True:
    pass # 무한루프주의
if 3 < 5:
    pass
def my_func():
    pass
'''



#예외처리
'''
try: 
 수행문장
except: 
 에러발생시수행문장
else: -> 옵션문장
 정상동작시수행문장
finally: -> 에러 발생 여부에 상관없이 수행됨
 마지막으로수행할문장 
'''
num1 = 3
num2 = 1
'''
try:
    result = num1 / num2
    print(f'연산결과는{result}입니다')

#except:
#    print('에러가발생했어요')

except ZeroDivisionError:
    print('0 으로나눌수없어요')
      
except TypeError:
    print('값의형태가이상해요')
      
except Exception as err:
    print('에러가발생했어요: ', err)
#> 실행결과: 에러가발생했어요: division by zero
    
else:
    print('정상동작했어요')

finally:
    print('수행종료')
'''



#모듈  ==  하나의 파이썬 파일(.py)  -> 변수, 함수, 클래스 등
import good
good.say()

from good import say   #from 상위개념 import 하위개념
say()

#from 파일 import 모듈  이런식으로도 가능
#모듈.함수()

# 프로젝트이름(워크스페이스) > 폴더이름(패키지) > 모듈(.py) > 클래스 > 함수,변수
# import. 은 내 위치에서 하위개념 열기 ..은 동위개념 열기 ...은 상위개념 열기

'''
from chap5 import good, bad     여러개 가능
good.say()
bad.bye()
'''