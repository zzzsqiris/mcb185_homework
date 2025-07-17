# 32 stats
# Iris Zhong
import sys
import statistics

# number of values
lst = []
for arg in sys.argv [1:]:
    lst.append(float(arg))
    num = len(lst)
print('number of value:', num)

# minium
min = lst[0]
for val in lst:
    if val <= min: min = val
print('minimum value:', min)

# maximum
max = lst[0]
for val in lst:
    if val >= max: max = val
print('maximum value', max)

# mean
total = 0
for val in lst:
    total += val
mean = total / len(lst)
print('mean:', f'{mean:.1f}')

# standard deviation
sd = statistics.stdev(lst)
print('standard deviation:', f'{sd:.1f}')

# median
index = len(lst) // 2
median = lst[index]
print('median:', median)