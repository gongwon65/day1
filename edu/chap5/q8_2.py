#Q8
numerator = 10
denominator = 0

try:
    result = numerator / denominator
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
else:    
    print("결과:", result)