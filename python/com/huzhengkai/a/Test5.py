import os
os.chdir('F:\\HeadFirstPython\\chapter3')
with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')
with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')
with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')
with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',')
print(james)
print(sorted(james))
print(julie)
print(mikey)
print(sarah)

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':'in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins,secs) = time_string.split(splitter)
    return (mins+'.'+secs)
a=[]
b=[]
c=[]
d=[]
for aa in james:
    a.append(sanitize(aa))
for bb in julie:
    b.append(sanitize(bb))
for cc in mikey:
    c.append(sanitize(cc))
for dd in sarah:
    d.append(sanitize(dd))
print(sorted(a))
print(sorted(b))
print(sorted(c))
print(sorted(d))

