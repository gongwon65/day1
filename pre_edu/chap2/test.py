#tuple
my_tuple = ('오예스', '몽쉘', '초코파이')
(pie1, pie2, pie3) = my_tuple
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
(one, *others, ten) = numbers
#투플의 경우 언패킹 시 리스트 형태 []로 나옴

#set
A = {'돈가스', '보쌈', '제육덮밥'}
B = {'짬뽕', '초밥', '제육덮밥'}
#print(A.intersection(B)), union(), difference()
#print(A[1]) 순서X 수정X
#.add, .remove, .clear, .del A -> 완전 삭제라 하면 A라는 세트가 없다고 나옴
A.update(B)

#딕셔너리 = {key1:value1, key2:value2, ... }
person = {'이름': '나귀욤', '나이': 7,'키': 120, '몸무게': 23}
#키는 중복불가 밸류는 가능
#print(person['이름']) 하면 해당 키키의 짝인 밸류가 나옴
person['최종학력']='유치원'
person['키']=130
person.update({'키':140, '몸무게':26})
person.pop('나이') #.clear() 모두삭제
#print(person.keys()) or person.values() 어떤 키나 벨류가 들었는지
#.items()하면 키와 벨류가 같이 나옴 -> 이 3가지는 중요!!!
 

#자료형 변환
#print(type(my_tuple))
my_list = list(my_tuple)
#print(type(my_list))
my_list.append('꼬북칩')
my_tuple = tuple(my_list)
#print(my_tuple)
#튜플은 수정이 안되지만 리스트로 변환 후 수정하고 다시 튜플로 변환시키면 됨
#중복이 필요없다면 세트. 다만 순서까지 생각해야한다면 딕셔너리로 변환
my_dic=dict.fromkeys(my_tuple)
#print(my_dic)
my_list = list(my_dic)
#print(my_list)
