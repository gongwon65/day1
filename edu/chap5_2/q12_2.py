#Q12
import random

num = []
while range(len(num) < 10):
    x = random.randint(1,101)
    if x not in num:
        num.append(x)
print(num)