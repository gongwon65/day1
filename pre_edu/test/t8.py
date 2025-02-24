f = open('t8list.txt', 'r')
lines = f.readlines()
print(lines,type(lines))
f.close()

lines.reverse()

f=open('t8list.txt', 'w')
for line in lines:
    line=line.strip()
    f.write(line)
    f.write('\n')
f.close()