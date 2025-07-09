# 22fibonacci.py
# Iris Zhong
'''
lst = []
while len(lst) < 10:
    if lst == []:
        n1 = 0
        n2 = 1
        lst.append(n1)
        lst.append(n2)
        print(lst)
    n1 = lst[-1]
    n2 = lst[-2]
    sum = n1 + n2
    lst.append(sum)
print(lst)
'''

def fib (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return (fib(n-1) + fib(n-2))

for i in range(10):
    print(fib(i))
    