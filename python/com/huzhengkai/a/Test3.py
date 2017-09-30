import os
os.chdir('F:\\HeadFirstPython\\chapter3')
print(os.getcwd())
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
try:
    man_file = open('man_data.txt','w')
    other_file = open('other_data.txt','w')
    print(man,file=man_file)
    print(other,file=other_file)
except IOError:
    print('File error...')
finally:
    man_file.close()
    other_file.close()







