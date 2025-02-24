'''
>> a, b, *c = (0, 1, 2, 3, 4, 5)
>> a
0
>> b
1
>> c
[2, 3, 4, 5]
'''

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, b, c = scores
print(valid_score)
a, *valid_score, c = scores
print(valid_score)



temp = {}
print(type(temp))
temp = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
print(temp)

temp['죠스바'] = 1200; temp['월드콘'] = 1500
print(temp)

print('메로나 가격: ', temp['메로나'])

temp['메로나'] = 1300
print(temp)

del temp['메로나']
print(temp)