a= '한글'
b = a.encode('euc-kr')
print(b, type(b))

a= 'life is too short'
b = a.encode('utf-8')
print(b, type(b))




import time

def elapsed(original_func):   # 기존 함수를 인수로 받는다.
    def wrapper():
        start = time.time()
        result = original_func()    # 기존 함수를 수행한다.
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))  # 기존 함수의 수행시간을 출력한다.
        return result  # 기존 함수의 수행 결과를 리턴한다.
    return wrapper

@elapsed
def myfunc():
    print("함수가 실행됩니다.")

# decorated_myfunc = elapsed(myfunc)  # @elapsed 데코레이터로 인해 더이상 필요하지 않다.
# decorated_myfunc()

myfunc()



# 이터레이터(iterator)란 무엇일까? 
# 이터레이터는 next 함수 호출 시 계속 그다음 값을 리턴하는 객체
# 즉, 이터와 next는 같이 있어야함.
a = [1, 2, 3]
ia = iter(a)
for i in ia:
    print(i)
for i in ia:
    print(i) #반복 안됨


# iterator.py
class MyItertor:
    def __init__(self, data):
        self.data = data
        self.position = 0

    def __iter__(self): # 반복행위가 일어날 때 자동으로 수행
        return self

    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result

if __name__ == "__main__":
    i = MyItertor([1,2,3])
    for item in i:
        print(item)
        
        




