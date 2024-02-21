import sys
import heapq
import copy

input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])
start, end = map(int, input().split())
dist = [INF] * (n+1)
dist[start] = 0


def dijkstra():
    hq = []
    heapq.heappush(hq, (0, start, [start, ]))
    while hq:
        cur_weight, cur_pos, cur_trace = heapq.heappop(hq)
        if cur_pos == end:
            print(dist[cur_pos])
            print(len(cur_trace))
            print(' '.join(map(str, cur_trace)))
            return
        if cur_weight != dist[cur_pos]:
            continue

        for nxt in graph[cur_pos]:
            n_end, n_weight = nxt[0], cur_weight + nxt[1]
            if dist[n_end] > n_weight:
                dist[n_end] = n_weight
                n_trace = copy.deepcopy(cur_trace)
                n_trace.append(n_end)
                heapq.heappush(hq, (n_weight, n_end, n_trace))


dijkstra()
