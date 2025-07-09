import random
import math
t = 1, 2  # this is a tuple
print(t)
print(type(t))

person = 'Steve', 21, 57891.50 # name, age, yearly income
print(person)

for i in range(5):
    print(random.random())

print("seed")
random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())

print("Pi")

count = 0
inside = 0
while True:
    count += 1
    x = random.random()
    y = random.random()
    distance = math.sqrt(x**2 + y**2)
    if distance < 1:
        inside += 1
    print((inside / count) * 4)