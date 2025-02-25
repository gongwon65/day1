for i in range(1, 7):
    file_name = f"q{i}.py"
    with open(file_name, 'w') as file:
        file.write("#Q1\n")
        #file.write("print('Hello, World!')\n")  # 기본 내용 예시로 추가
    print(f"{file_name} has been created.")