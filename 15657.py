from itertools import combinations_with_replacement

N, M = map(int, input().split())
numAry = sorted(list(map(int, input().split())))
combs = combinations_with_replacement(numAry, M)

for comb in combs:
    print(' '.join(map(str, comb)))
