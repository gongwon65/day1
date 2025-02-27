

'''''
#2
result = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        result
        '''
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
'''
'''
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
tab_content=f.read()
f.close()


tab_content = tab_content.replace("/t", " "*4)

fw = open(dst, 'w')
fw.write(space_content)
fw.close
'''



#6
r'''
import os
#재귀함수: 자신을 호출
#스택이라는 개념이 선행되어야 함. 엘레베이터 처음 탄 사람이 마지막에 나오는 개념
#재귀는 스택 개념이기에 재귀를 했을 시 재귀한것이 끝나야 처음이 수행됨.
#반드시 종료 조건이 포함되어야 함
def search(dirname):
    try:
        filenames=os.listdir(dirname) #dirname안의 파일 리스트를 리턴
        print(filenames)
        for filename in filenames:
            full_filename = os.path.join(dirname,filename) #디렉토리와 파일이름을 합침
            if os.path.isdir(full_filename): #dict인지 file인지 구분
                search(full_filename) #dict라면 다시 search함수를 호출해 그 폴더를 재 서칭
            else:
                ext=os.path.splitext(full_filename)[-1]
                if ext=='.py':
                    print(full_filename)
                    
    except PermissionError: #수행권한이 없는 폴더에 접근할 때때
        #pass
        print('접근권한 없없음')
search(r'C:\Users\302-1\gongwon\pre_edu')
'''
r'''
import os
for (path, dir, files) in os.walk(r'C:\Users\302-1\gongwon\pre_edu'):
    for filename in files:
        #print(path, dir, files)
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print('%s/%s' % (path, filename))
'''















