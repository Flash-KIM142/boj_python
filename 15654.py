from itertools import permutations

N, M = map(int, input().split())
numAry = list(map(int, input().split()))
result = list(permutations(numAry, M))
result.sort()
for perm in result:
    print(' '.join(map(str, perm)))
