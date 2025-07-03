import math

def char_to_prob(c):
    Q = ord(c) - 33
    p = 10 ** (-Q / 10)
    return p

def prob_to_char(p):
    Q = int(-10 * math.log10(p))
    return chr(Q + 33)

print(char_to_prob('A'))
print(prob_to_char(0.001))