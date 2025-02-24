#1
#shirt

#2
i=1
result = 0
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)


#3
a=0
while True:
    a+=1
    if a > 5:
        break
    print('*'*a)


#4
#for x in range(1,101,1):
#    print(x)

#5
A=[70,60,55,75,95,90,80,80,85,100]
total=0
for score in A:
    total += score
average = total / len(A)
print(average)

numbers = [1,2,3,4,5]

result = [n*2 for n in numbers if n%2==1]
print(result)