import sys
import heapq

input = sys.stdin.readline
INF = float('inf')
n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    c1, c2, w = map(int, input().split())
    graph[c1].append([c2, w])
    graph[c2].append([c1, w])

hq = []
heapq.heappush(hq, (0, 1, k))
dist = [[INF] * (n + 1) for _ in range(k + 1)]
dist[k][1] = 0

while hq:
    cur_time, cur_pos, cur_chance = heapq.heappop(hq)
    if dist[cur_chance][cur_pos] < cur_time:
        continue
    for nxt in graph[cur_pos]:
        nxt_time, nxt_pos = cur_time + nxt[1], nxt[0]
        if dist[cur_chance][nxt_pos] > nxt_time:
            dist[cur_chance][nxt_pos] = nxt_time
            heapq.heappush(hq, (nxt_time, nxt_pos, cur_chance))
        if cur_chance > 0 and dist[cur_chance - 1][nxt_pos] > cur_time:
            dist[cur_chance - 1][nxt_pos] = cur_time
            heapq.heappush(hq, (cur_time, nxt_pos, cur_chance - 1))

answer = INF
for i in range(k+1):
    answer = min(answer, dist[i][n])
print(answer)
