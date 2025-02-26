for _ in range(5):
    print('hi')

dic = [['hey', 'underscore',], ['come', 'with me']]
for _, second in dic:
    print(_)


money = 10_000_000
print( money + 1 )


class Myclass():
    def __init__(self):
        self.__variable = 10
        self.abc=20

    def func(self):
        print('>>>', self.__variable)

obj = Myclass()
obj.func()
print(obj.abc)           #맹글링(magling)
'''print(obj.__variable)''' #_(언더바)를 2개 쓴 변수는 내부에서만 접근이 가능
#print(obj._Myclas__variable) #그래서 _Myclass__variable로 호출해야 외부에서 가능

name = 10
def hi():
    name = 20
    print(name)
    
'''
if __name__ == "_main_":
    print('직접 실행했을때만 출력됨')
'''