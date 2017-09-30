from functools import reduce
f = abs
a = f(-20)
print(a)

def add(x, y, f):
    return f(x) + f(y)
aa = add(-5, 6, abs)
print(aa)

print('*******************************')
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
bb = list(r)
print(bb)

print('*******************************')



print('*******************************')

def add(x, y):
    return x + y
ab = reduce(add, [1, 3, 5, 7, 9])
print(ab)

print('*******************************')

def is_odd(n):
    return n % 2 == 1

abc = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(abc)

aaaa = sorted([36, 5, -12, 9, -21])
print(aaaa)

abb = sorted([36, 5, -12, 9, -21], key=abs)
print(abb)

print('*******************************')

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())

