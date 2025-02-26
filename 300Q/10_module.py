import datetime

now = datetime.datetime.now()
print(now, type(now))

for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day) 
    date = now - delta
    print(date)
    
    


now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))




day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))


'''
import time
import datetime

start_time = time.time()  # 프로그램 시작 시간 기록
duration = 10  # 10초 후에 종료

while True:
    now = datetime.datetime.now()
    print(now)
    time.sleep(1)
    
    if time.time() - start_time >= duration:
        print("10 seconds passed. Exiting...")
        break
'''

import os
ret = os.getcwd()
print(ret, type(ret))
r'''
os.rename(r"C:\Users\302-1\gongwon\pre_edu\명령어2.txt",
           r"C:\Users\302-1\gongwon\pre_edu\명령어.txt")
'''

'''
import numpy
for i in numpy.arange(0, 5, 0.1):
    print(i)
'''   