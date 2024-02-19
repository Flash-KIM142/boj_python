from itertools import product

N, M = map(int, input().split())
numAry = list(map(int, input().split()))
combs = sorted(product(numAry, repeat=M))

for comb in combs:
    print(' '.join(map(str, comb)))
