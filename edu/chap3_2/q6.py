# This is q6.py
numbers = [1,2,3,4,5]

result = [x*2 for x in numbers if not x % 2 == 0]
print(result)
