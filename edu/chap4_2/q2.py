#Q2
def is_prime(n):
    if n <= 1:
        return False
    
    elif n == 2:
        return True
    
    elif n % 2 == 0:
        return False
    
    else:
        for i in range(3, n, 2):
            if n % i == 0:
                return False
        return True


print(is_prime(17))