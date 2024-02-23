import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    v1, v2, w = map(int, input().split())
    graph[v1].append([v2, w])
    graph[v2].append([v1, w])

t1, t2 = map(int, input().split())


def dijkstra(start, end):
    dist = [INF] * (n + 1)
    dist[start] = 0

    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        cur_weight, cur_pos = heapq.heappop(hq)
        if cur_weight > dist[cur_pos]:
            continue

        for nxt in graph[cur_pos]:
            nxt_pos, nxt_weight = nxt[0], cur_weight + nxt[1]
            if dist[nxt_pos] > nxt_weight:
                dist[nxt_pos] = nxt_weight
                heapq.heappush(hq, (nxt_weight, nxt_pos))

    return dist[end]


result = min(dijkstra(1, t1) + dijkstra(t1, t2) + dijkstra(t2, n),
             dijkstra(1, t2) + dijkstra(t2, t1) + dijkstra(t1, n))
if result >= INF:
    print(-1)
else:
    print(result)
