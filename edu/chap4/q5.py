#Q5
def p_f():
    txt = input('내용을 입력하십시오: ')
    with open('input.txt', 'w', encoding='utf8') as f:
        f.write(txt)

p_f()
    