import os
os.chdir('F:\\HeadFirstPython\\chapter3')
print(os.getcwd())
os.getcwd()
man = []
other = []
try:
    data = open('sketch.txt',encoding='utf-8')
    for each_line in data:
        try:
            (role,line_spoken) = each_line.split(':',1)
            #去除空白字符
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')
print(man)
print(other)