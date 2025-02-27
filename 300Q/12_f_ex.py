r'''
with open('매수종목2.txt', 'w', encoding='utf-8') as f:
    f.write('005930 \n')
    f.write('005380 \n')
    f.write('035420 \n')
'''

r'''
import csv

with open(r"C:\Users\302-1\gongwon\300Q\매수종목.csv", "w", encoding="cp949", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["종목명", "종목코드", "PER"])
    writer.writerow(["삼성전자", "005930", 15.59])
    writer.writerow(["NAVER", "035420", 55.82])
''' 



'''
with open('매수종목2.txt','r',encoding='utf-8')as f:
    lines = f.readlines()   

codes = []
for line in lines:
    code = line.strip()  #'\n'
    codes.append(code)

print(codes)
'''

'''
f = open("매수종목2.txt", mode="wt", encoding="utf-8")
f.write("005930 삼성전자\n")
f.write("005380 현대차\n")
f.write("035420 NAVER\n")
f.close()


f = open("매수종목2.txt", encoding="utf-8")
lines = f.readlines()

data = {}
for line in lines:
    line = line.strip()     # '\n' 제거
    k, v = line.split()
    #print(k, v)
    data[k] = v

print(data)
f.close()
'''