# Iris Zhong

import sys
seq = sys.argv[1]
match = sys.argv[2]
mismatch = sys.argv[3]

for letter in seq:
    print(letter, end = '   ')
print()

for nt1 in seq:
    print(nt1, end = '  ')
    