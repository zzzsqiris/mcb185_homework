# 10demo.py by Iris Zhong
import math

print('hello, again') # greeting
print(pow(2,3))
print(round(3.14159265, ndigits=3))
print(math.e)
print(math.ceil(3.1415))
print(0 / math.inf)
print(0.1 * 3)
print((0.1 + 0.2) != 0.3)

a = 3                       # side of triangle
b = 4                       # side of triangle
c = math.sqrt(a**2 + b**2)  # hypotenuse
print(c)
print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=', ', end='!\n')

def pythagoras(a, b): return math.sqrt(a**2 + b**2)
print(pythagoras(3, 4))

def findmean(c, d, e): return ((c + d + e) / 3)
print(findmean(5, 15, 10))

a = 0.3
b = 0.1 * 3
if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')