# 23triples.py
# Iris Zhong

import math

for a in range (1, 100):
    for b in range (1, 100):
        c = math.sqrt(a**2 + b **2)
        if c % 1 == 0 and a < b:
            print(a, b, int(c))