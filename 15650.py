from itertools import combinations

N, M = map(int, input().split())
ary = []
for i in range(1, N+1):
    ary.append(i)
combs = list(combinations(ary, M))
combs.sort()

for comb in combs:
    print(' '.join(str(num) for num in comb))