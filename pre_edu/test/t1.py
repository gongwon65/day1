
a = 'a:b:c:d'
'''
print(a)
split_a = a.split(':')
print(split_a)
join_a = '#'.join(split_a)
print(join_a)
'''
print('#'.join(a.split(':')))
