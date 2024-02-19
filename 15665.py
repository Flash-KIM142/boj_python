from itertools import product

N, M = map(int, input().split())
numAry = sorted(map(int, input().split()))
result = list(product(numAry, repeat=M))
result = sorted(list(set(result)))

for cur in result:
    print(' '.join(map(str, cur)))
