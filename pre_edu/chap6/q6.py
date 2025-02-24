

'''''
#2
result = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        result
        '''

#3
def getTotalPage(m,n):
    if m% n == 0:
        return m//n
    return m//n +1

print(getTotalPage(5,10))
print(getTotalPage(15,10))
print(getTotalPage(25,10))
print(getTotalPage(30,10))

'''''
#4
import sys
option = sys.argv[1]

if option=='-a':
    memo=sys.argv[2]
    f=open('memo.txt','a')
    f.write(memo)
    f.write('\n')
    f.close()

elif option == '-v':
    f=open('memo.txt', 'a')
    memo=f.read()
    f.close()
    print(memo)
'''

'''''
#5
import sys
src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = tab_content.replace("/t")
'''



#6
'''''
import os
def search(dirname):
    try:
        filenames=os.listdir(dirname)
        print(filenames)
        for filename in filenames:
            full_filename = os.path.join(dirname,filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext=os.path.splitext(full_filename)[-1]
                if ext=='.py':
                    print(full_filename)
    except PermissionError:
        pass
search('C:\gongwon\chap6')
'''

import os
for (path, dir, files) in os.walk('C:\gongwon\chap6'):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print('%s/%s' % (path, filename))
















