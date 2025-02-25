리스트 = [100, 200, 300]
for x in 리스트:
    print(x + 10)
    


리스트 = ["김밥", "라면", "튀김"]
for x in 리스트:
    print('오늘의 메뉴:', x)
    
    

리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for 길이 in 리스트:
    print(len(길이))
    



리스트 = ['dog', 'cat', 'parrot']
for x in 리스트:
    print(x, len(x))


for x in 리스트:
    print(x[0])




리스트 = [1, 2, 3]
for x in 리스트:
    print(f'3 x {x} = {3*x}')



리스트 = ["가", "나", "다", "라"]
for x in reversed(리스트):
    print(x)




리스트 = [3, -20, -3, 44]
for x in 리스트:
    if x <0:
        print(x)




리스트 = ["I", "study", "python", "language", "!"]
for x in 리스트:
    if len(x) >= 3:
        print(x)


리스트 = ["A", "b", "c", "D"]
for x in 리스트:
    if x.islower():
        print(x)


리스트 = ['dog', 'cat', 'parrot']
for 변수 in 리스트:
    print(변수.capitalize())



리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for x in 리스트:
    y = x.split('.')
    print(y[0])



for x in range(100):
    print(x)


for x in range(2002,2051,4):
    print(x)




for x in range(3,31,3):
    print(x)
    





for x in range(100):
    print(99-x)




for x in range(10):
    print(f'{x/10:.1f}')
    
    


for x in range(1,10):
    print(f'3x{x} = {x*3}')


total = 1
for x in range(1,11):
    total*=x
print(total)





price_list = [32100, 32150, 32000, 32500]
for x in range(len(price_list)):
    print(price_list[x])




#enumerate 객체의 인덱스와 값을 같이 반환
price_list = [32100, 32150, 32000, 32500]
for i, data in enumerate(price_list):
    print(i, data)



my_list = ["가", "나", "다", "라"]
for x in range(3):
    print(my_list[x], my_list[x+1])



my_list = [100, 200, 400, 800]
for x in range(3):
    print(my_list[x+1]-my_list[x])


my_list = [100, 200, 400, 800, 1000, 1300]

for x in range(len(my_list)-3):
    print((my_list[x]+my_list[x+1]+my_list[x+2])/3)


volatility = []
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
'''
for x in range(len(low_prices)):
    volatility.append(high_prices[x]-low_prices[x])
print(volatility)
'''
리스트 = [0,1,2,3,4]
volatility = [high_prices[x]-low_prices[x] for x in 리스트]
print(volatility)


apart = [ ["301호", "302호"], ["201호", "202호"], ["101호", "102호"] ]
for x in apart:
    print(x)



apart = [ [101, 102], [201, 202], [301, 302] ]
for float in apart:
    for number in float:
        print(number, "호")