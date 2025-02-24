'''
today = '토요일'
if today =='일요일':
    print('게임 한 판')
elif today == '토요일':
    print('물 한 잔')
else:
    print('폰 5분')
print('공부시작')
'''

yellow_card = 1
foul = True
if foul:
    yellow_card += 1
    if yellow_card == 2:
        print('경고 누적 퇴장')
    else:
        print('휴.. 조심해야지')
else:
    print('주의')


#for 반복문
for x in range(1): #임시변수, 반복대상 또는 범위 range(start,stop,step)
    print(f'팔 벌려{x}회 뛰기') 

my_list = [1, 2, 3]
for x in my_list :
    print(x)
#딕셔너리의 경우 for x in person.valuse(): keys
#items은 투플로 묶여서 나오기때문에 for x,y in person.items로 실행해도 됨



#while   for가 정해진 만큼이면 while은 일단 계속 진행. 즉, 무한
max = 25 
weight = 0 
item = 3 
while weight + item <= max:
    weight += item
    #print(f'짐을 추가합니다. 현재 무게:{weight}입니다')
#print(f'총 무게는 {weight} 입니다')


#break 반복문 탈출
drama = ['시즌1', '시즌2', '시즌3', '시즌4', '시즌5']
for x in drama:
    if x == '시즌3':
        print('재미 없대, 그만 보자')
        break
    #print(f'{x} 시청')
#break가 없다면 시청 시청 재미없음 시청 시청까지 감

'''
#continue
continue가 없으면 시즌1 시즌2 (재미없음 시즌3) 시즌4 시즌5
있으면 시즌1 시즌2 재미없음 시즌4 시즌5  ㄴ> if를 진행한것과 안한것 둘다 존재
'''

#리스트 컴프리헨션
products=['JOA-2020','JOA-2021', 'SIRO-2020', 'SIRO-2022']
recall=[]
for p in products:
    if p.startswith('SIRO'):
         recall.append(p)
#print(recall)

#new_list = [변수 활용 for 변수 in 리스트 if 조건]
my_list = [1, 2, 3, 4, 5]
new_list = [x for x in my_list if x > 3]

'''
 x        # [1, 2, 3, 4, 5]
 x + 1    # [2, 3, 4, 5, 6]
 x * 3    # [3, 6, 9, 12, 15]
 str(x) + “번째”     # [“1번째”, “2번째”, “3번째”, ...]
여기서 3이하 숫자를 활용한 것은 제외될 것임
'''