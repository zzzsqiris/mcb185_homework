# Iris Zhong
def tm(A, C, T, G):
    oligos = A + C + T + G
    if oligos <= 13: Tm = (A+T)*2 + (G+C)*4
    else: Tm = 64.9 + 41*(G+C -16.4) / (A+T+G+C)
    return Tm

print(tm(5, 7, 3, 4))