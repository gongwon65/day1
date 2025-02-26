
for i in range(3, 14):
    file_name = f"q{i}_2.py"
    with open(file_name, 'w', encoding = 'utf8') as f:
        f.write(f"#Q{i}\n")
        #f.write("print('Hello, World!')\n")  # 기본 내용 예시로 추가
    print(f"{file_name} has been created.")



'''
import os

# q1.py ~ q6.py 파일 삭제
for i in range(1, 7):
    file_name = f"q{i}.py"
    if os.path.exists(file_name):  # 파일이 존재하는지 확인
        os.remove(file_name)
        print(f"{file_name} has been deleted.")
    else:
        print(f"{file_name} does not exist.")
'''