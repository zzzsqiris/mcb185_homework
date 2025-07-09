# savingthrows.py
# Iris Zhong

import random

def throw(dc, condition):
    win_count = 0
    n = 1000000
    if condition == "normal":
        for i in range (n):
            if random.randint(1, 20) >= dc:
                win_count += 1
    elif condition == "advantage":
       for i in range (n):
            max_dice = max(random.randint(1, 20), random.randint(1, 20))
            if max_dice >= dc:
                win_count += 1
    elif condition == "disadvantage":
        for i in range (n):
            min_dice = min(random.randint(1, 20), random.randint(1, 20))
            if min_dice >= dc:
                win_count += 1
    p = win_count / n
    return p


print("DC", "Normal", "Advantage", "Disadvantage", sep = "\t")
print("5", throw(5, "normal"), throw(5, "advantage"), throw(5, "disadvantage"), sep = "\t")
print("10", throw(10, "normal"), throw(10, "advantage"), throw(10, "disadvantage"), sep = "\t")
print("15", throw(15, "normal"), throw(15, "advantage"), throw(15, "disadvantage"), sep = "\t")