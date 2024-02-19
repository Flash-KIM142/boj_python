from itertools import combinations

N, M = map(int, input().split())
numAry = sorted(list(map(int, input().split())))
combs = list(combinations(numAry, M))
combs.sort()

for comb in combs:
    print(' '.join(map(str, comb)))
