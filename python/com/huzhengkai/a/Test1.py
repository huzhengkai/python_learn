import os
os.chdir('F:\\HeadFirstPython\\chapter3')
print(os.getcwd())
data = open('sketch.txt',encoding='utf-8')
print(data)
try:
    print(os.path.exists('sketch.txt'))
    for each_line in data:
        try:
            (role,line_spoken) = each_line.split(':',1)
            print(role,end='')
            print(' said: ',end='')
            print(line_spoken,end='')
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')
