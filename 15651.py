from itertools import product

N, M = map(int, input().split())
ary = []
for i in range(1, N + 1):
    ary.append(i)
combs = list(product(ary, repeat=M))
combs.sort()

for comb in combs:
    print(' '.join(map(str, comb)))

# def backtracking():
#     if len(s) == m:
#         print(' '.join(map(str, s)))
#         return
#     for i in range(1, n + 1):
#         s.append(i)
#         backtracking()
#         s.pop()
#
#
# n, m = map(int, input().split())
# s = []

# backtracking()