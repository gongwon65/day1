result = 0
try:
    [1,2,3][3]  # 이게 뭔지 모름 error 발생생
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)