my_variable = ()
print(type(my_variable))



movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
print(movie_rank)
num = (1,)
#하나의 데이터를 저장할 시 ,를 입력하지 않으면 튜플로 인식되지 않는다.
print(num)

t = 1, 2, 3, 4
print(type(t))




interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest_list = list(interest)
print(interest_list)
interest_tuple = tuple(interest_list)
print(interest_tuple)



temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)



data = tuple(range(2,100,2))
print(data)



