import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
col, row = map(int, input().split())
map_ary = [list(map(int, input().strip())) for _ in range(row)]
break_cnt = [[INF for _ in range(col)] for _ in range(row)]
break_cnt[0][0] = 0

hq = []
heapq.heappush(hq, (0, 0, 0))

while hq:
    cur_cnt, cur_r, cur_c = heapq.heappop(hq)
    if break_cnt[cur_r][cur_c] < cur_cnt:
        continue

    for d_r, d_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        n_r, n_c = d_r + cur_r, d_c + cur_c
        if n_r < 0 or n_r >= row or n_c < 0 or n_c >= col:
            continue
        n_cnt = cur_cnt + map_ary[n_r][n_c]
        if break_cnt[n_r][n_c] > n_cnt:
            break_cnt[n_r][n_c] = n_cnt
            heapq.heappush(hq, (n_cnt, n_r, n_c))

print(break_cnt[row-1][col-1])
