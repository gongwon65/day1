class Human():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    '''
    def __del__(self):
        print("나의 죽음을 알리지마라")
    '''
    
    def who(self):
        print(f'이름: {areum.name}, 나이: {areum.age}, 성별: {areum.sex}')
    
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    



'''
areum = Human("불명", "미상", "모름")
areum.who()      

areum.setInfo("아름", 25, "여자")
areum.who() 
'''

areum = Human("아름", 25, "여자")
#del(areum)
#areum.who()


class OMG : 
    def print(self) :
        print("Oh my god")
        
#mystock = OMG()
#mystock.print()



'''
class Stock:
    
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

종목 = []

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
    print(i.code, i.per)
'''














#281
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
    
    def 정보(self):
        print('바퀴수:', self.바퀴)
        print("가격: ", self.가격)

car = 차(2,1000)
#print(car.바퀴)
#print(car.가격)



class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계
    def 정보(self):
        super().정보()
        print("구동계: ", self.구동계)

bicycle = 자전차(2, 100, "시마노")
#print(bicycle.구동계)
#print(bicycle.바퀴)
#bicycle.정보()


class 자동차(차):
    def 정보(self):
        print('바퀴수:', self.바퀴)
        print("가격: ", self.가격)
        
car = 자동차(4, 1000)
#car.정보()


class 부모:
    def __init__(self):
        print("부모생성")

class 자식(부모):
    def __init__(self):
        print("자식생성")
        super().__init__()

나 = 자식()