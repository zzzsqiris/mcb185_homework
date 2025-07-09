# deathsaves.py
# Iris Zhong
import random

trial = 10000
die_count = 0
stable_count = 0
revive_count = 0

for i in range(trial):
    fail_count = 0
    success_count = 0
    while fail_count < 3 and success_count < 3:
        dice = random.randint(1,20)
        if dice == 1:
            fail_count += 2
        elif dice == 20:
            revive_count += 1
            break
        elif dice < 10:
            fail_count += 1
        elif dice >= 10:
            success_count += 1
    if fail_count >= 3: 
        die_count += 1
    elif success_count >= 3: 
        stable_count += 1

print("p dies:", die_count / trial)
print("p stable:", stable_count / trial)
print("p revive:", revive_count / trial)
