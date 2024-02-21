from collections import deque

map_ary = [input() for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
answer = 0


def bfs(i, j):
    q = deque()
    tmp_visited = [[0] * 5 for _ in range(5)]

    q.append((i, j))
    tmp_visited[i][j] = 1
    res = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < 5 and 0 <= nj < 5 and tmp_visited[ni][nj] == 0 and visited[ni][nj] == 1:
                q.append((ni, nj))
                tmp_visited[ni][nj] = 1
                res += 1

    return res == 7


def check_adjacent():
    for i in range(5):
        for j in range(5):
            if visited[i][j] == 1:
                return bfs(i, j)


def backtracking(n, cnt, s_cnt):
    global answer
    if cnt > 7:
        return
    if n == 25:
        if cnt == 7 and s_cnt >= 4:
            if check_adjacent():
                answer += 1
        return

    visited[n // 5][n % 5] = 1
    backtracking(n + 1, cnt + 1, s_cnt + int(map_ary[n // 5][n % 5] == 'S'))
    visited[n // 5][n % 5] = 0
    backtracking(n + 1, cnt, s_cnt)


backtracking(0, 0, 0)
print(answer)
