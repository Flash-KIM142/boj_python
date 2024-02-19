from itertools import permutations

N, M = map(int, input().split())
numAry = sorted(list(map(int, input().split())))
combs = permutations(numAry, M)
combs = sorted(list(set(combs)))

for comb in combs:
    print(' '.join(map(str, comb)))
