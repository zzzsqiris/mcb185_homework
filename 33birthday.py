# Iris Zhong

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

def check_duplicate(days, people):
    lst = []
    for ppl in range (people):
        date = random.randint(1, days)
        if date in lst:
            return True
        else:
            lst.append(date)

duplicate = 0
for i in range(trials):
    if check_duplicate(days, people) == True:
        duplicate += 1

prob = duplicate / trials
print(prob)