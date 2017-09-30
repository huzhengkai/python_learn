from collections import Iterable
from collections import Iterator
a = [x * x for x in range(1, 11)]
#print(type(a))
g = (x * x for x in range(10))
#for n in g:
#   print(n)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
o = odd()
print(next(o))
print(next(o))
print(next(o))
#print(next(o))

a = isinstance([], Iterable)
print(a)
b = isinstance((x for x in range(10)), Iterator)
print(b)
c = isinstance([], Iterator)
print(c)
d = isinstance({}, Iterator)
print(d)

e = isinstance(iter([]), Iterator)
print(e)
