import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
dist = [INF] * (v+1)
dist[k] = 0
for _ in range(e):
    start, end, weight = map(int, input().split())
    graph[start].append([end, weight])


def dijkstra(s):
    pq = []
    heapq.heappush(pq, (0, s))
    while pq:
        cur_weight, cur_pos = heapq.heappop(pq)
        if cur_weight > dist[cur_pos]:
            continue

        for nxt in graph[cur_pos]:
            n_end, n_weight = nxt[0], cur_weight + nxt[1]
            if dist[n_end] > n_weight:
                dist[n_end] = n_weight
                heapq.heappush(pq, (n_weight, n_end))


dijkstra(k)

for i in range(1, v+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
