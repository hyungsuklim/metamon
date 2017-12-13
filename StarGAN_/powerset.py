from itertools import chain, combinations
import numpy as np

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def subsets(s):
    return map(set, powerset(s))
'''
l = ['H', 'A', 'G']
s = list(powerset(l))
print(s)
for i in range(len(l)+1):
    s.pop(0)

L = [[],[],[]]
for i, x in enumerate(s):
    if 'H' in x:
        L[0].append(i)
    if 'A' in x:
        L[1].append(i)
    if 'G' in x:
        L[2].append(i)

print(L)
for i in range(len(l)+1):
    s.pop(0)
print(s)'''
