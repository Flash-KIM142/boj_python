def backtracking(idx):
    if len(cur) == M:
        print(' '.join(map(str, cur)))
        return

    for i in range(idx, N + 1):
        cur.append(i)
        backtracking(i)
        cur.pop()


N, M = map(int, input().split())
cur = []
backtracking(1)
