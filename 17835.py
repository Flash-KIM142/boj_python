import sys
import heapq

input = sys.stdin.readline
INF = float('inf')
n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, c = map(int, input().split())
    graph[v].append([u, c])
interview = list(map(int, input().split()))


def dijkstra():
    dist = [INF] * (n + 1)
    ans_city = 0
    ans_dist = 0

    hq = []
    for i in interview:
        dist[i] = 0
        heapq.heappush(hq, (0, i))
    while hq:
        cur_weight, cur_pos = heapq.heappop(hq)
        if cur_weight > dist[cur_pos]:
            continue

        for nxt in graph[cur_pos]:
            nxt_pos, nxt_weight = nxt[0], cur_weight + nxt[1]
            if dist[nxt_pos] > nxt_weight:
                dist[nxt_pos] = nxt_weight
                heapq.heappush(hq, (nxt_weight, nxt_pos))

    for i in range(1, n + 1):
        if dist[i] != INF and dist[i] > ans_dist:
            ans_city, ans_dist = i, dist[i]

    return ans_city, ans_dist


city, dist = dijkstra()
print(city)
print(dist)
