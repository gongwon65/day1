#Q4
import random

num = []

while len(num) < 11:
    rand = random.randint(1,100)
    if rand not in num:
        num.append(rand)
num.sort()
print(num)


