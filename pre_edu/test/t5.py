input = int(input('숫자 입력:'))

def fib(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)

for i in range(input):
    print(fib(i))


