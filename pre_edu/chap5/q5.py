#1
class Calculator:
  def __init__(self):
    self.value = 0

  def add(self, val):
    self.value += val
    

class UpgradeCalculator(Calculator):
  def minus(self, val):
    self.value -= val
    

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)



#2

class MaxLimitCalculator(Calculator):
  def add(self, val):
    self.value += val
    if self.value >=100:
      self.value = 99


cal2 = MaxLimitCalculator()
cal2.add(50)
print(cal2.value)
cal2.add(60)
print(cal2.value)


#3
print(all([1,2,abs(-3)-3]))
print(chr(ord('a'))=='a')

#4
print(list(filter(lambda x: x>0,[1,-2,3,-5,8,-3])))

#5
print(int('0xea',16))

#6
print(list(map(lambda x: x*3, [1,2,3,4])))

#7
a = [-8,2,7,5,-3,5,0,1]
print(max(a)+min(a))

#8
print(round(17/3,4))


'''''
import sys
num = sys.argv[1:]
result = 0
for i in num:
  result += int(i)
print(result)
  '''
  
'''''
import os
os.chdir('C:\gongwon')
f = os.popen('gongwon')
print(f.read())
'''

#11
#import glob
#print(glob.glob('C:\gongwon\chap5\*.py'))

#12
#import time
#print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time())))




#13
'''
import random
result = []
while len(result) < 6:
  num = random.randint(1,45)
  if num not in result:
    result.append(num)

print(result)
'''