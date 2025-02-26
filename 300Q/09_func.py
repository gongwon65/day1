

'''
def print_with_smile():
    user = input('글을 써주세요: ')
    return user+' :D'
print(print_with_smile())
'''
#굳이 사용자한테 입력받을 필요는 없었음.


def print_with_smile (string) :
    print (string + ":D")

print_with_smile('안녕하세요')


def print_upper_price(price):
    print(f'{price*1.3:.2f}')


def print_sum(num1, num2):
    print(num1 + num2)
    

def print_arithmetic_operation(num1, num2):
    print(num1, '+', num2, '=', num1 + num2)
    print(num1, '-', num2, '=', num1 - num2)
    print(num1, '*', num2, '=', num1 * num2)
    print(num1, '/', num2, '=', num1 / num2)


def print_max(a,b,c):
    max_val = 0
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)

def print_keys(dic):
    for keys in dic.keys():
        print(keys)
#print_keys({"이름":"김말똥", "나이":30, "성별":0})


my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(dic, date):
    print(dic[date])



'''
def print_5xn(line):
    chunk_num = int(len(line) / 5)
    for x in range(chunk_num + 1) :
        print(line[x * 5: x * 5 + 5])
'''        
        
def printmxn(line, num):
    chunk_num = int(len(line) / num)
    for x in range(chunk_num + 1) :
        print(line[x * num: x * num + num])
#printmxn("아이엠어보이유알어걸", 2)


def calc_monthly_salary(annual_pay):
    monthly_pay = int(annual_pay / 12)  #int는 소수점을 버리고 정수로 치환환
    # print(monthly_pay)                  #반올림을 원한다면 round
calc_monthly_salary(12000000)





def pickup_even(list):
    new_list = [x for x in list if x%2 == 0]
    print(new_list)

pickup_even([3, 4, 5, 6, 7, 8])


'''
def convert_int(string):
    return int(string.replace(',', ''))
'''
def convert_int(string):
    num = string.split(',')
    print(int(''.join(num)))
convert_int("1,234,567")







