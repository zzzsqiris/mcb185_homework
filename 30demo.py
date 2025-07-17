import math
s1 = 'hey "dude" don\'t tell me what to do'
print(s1)
s = 'hello world'
print(s.count(s1))
print(s.upper())
print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))

print(f'{math.pi}')            # does nothing special
print(f'{math.pi:.3f}')        # 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')    # exponent notation
print(f'{"hello world":>20}')  # right justify with space filler
print(f'{"hello world":.>20}') # right justify with dot filler
print(f'{20:<10} {10}')        # left justify

print(f'{"hello world":<10} {2e5 * math.pi:e}')
print('{} {:.3f}'.format('str.format', math.pi))

seq = 'GAATTC'
for nt in seq:
    print(nt, end="")
print()

for i in range(len(seq)):
    print(i, seq[i])

s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])
print(s[::])
print(s[::-1])
print(s, s[::], s[::1], s[::-1])

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    print(i, codon)

nts = 'ACGT'
for i in range(len(nts)):
    print(i, nts[i])

for i, nt in enumerate(nts):
    print(i, nt)
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)
nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)
alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)
text = 'good day          to you'
words = text.split()
print(words)
s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)