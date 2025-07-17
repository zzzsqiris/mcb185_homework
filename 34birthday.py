# Iris Zhong

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

def check_duplicate(days, people):
    calendar = [0] * days
    for ppl in range (people):
        date = random.randint(0, days-1)
        calendar[date] += 1
    if max(calendar) > 1:
        return True
    return False

duplicate = 0
for i in range(trials):
    if check_duplicate(days, people) == True:
        duplicate += 1

prob = duplicate / trials
print(prob)