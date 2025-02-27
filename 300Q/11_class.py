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
areum.who()


class OMG : 
    def print(self) :
        print("Oh my god")
        
mystock = OMG()
mystock.print()




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