from itertools import combinations

N, M = map(int, input().split())
numAry = sorted(map(int, input().split()))
combs = list(combinations(numAry, M))
combs = sorted(list(set(combs)))

for comb in combs:
    print(' '.join(map(str, comb)))
