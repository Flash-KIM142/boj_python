from itertools import combinations

while True:
    ary = list(map(int, input().split()))
    if ary[0] == 0:
        break

    s = ary[1:]
    combs = sorted(list(combinations(s, 6)))
    for comb in combs:
        print(' '.join(map(str, comb)))
    print()
