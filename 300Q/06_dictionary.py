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



inventory = {'메로나':[300,20], '비비빅':[400,3], '죠스바':[250,100]}
print(inventory)

print(inventory['메로나'][0],'원')
print(inventory['메로나'][1], '개')

inventory['월드콘'] = [500,7]
print(inventory)

ice_name = list(inventory.keys())
print(ice_name)

ice_name = list(inventory.values())
print(ice_name)



icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)



keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)
