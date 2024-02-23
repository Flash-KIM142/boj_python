import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline
n, m, x = map(int, input().split())
graph = [[] for _ in range(m+1)]
for i in range(m):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])

result = [[] for _ in range(n+1)]


def dijkstra_to_party(start):
    dist = [INF] * (n+1)
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

    return dist[x]


# 모든 지점으로부터 파티 지점으로까지의 최단 거리 구하기
for i in range(1, n+1):
    if i == x:
        result[i].append(0)
        continue
    result[i].append(dijkstra_to_party(i))


def dijkstra_to_home():
    dist = [INF] * (n + 1)
    dist[x] = 0

    hq = []
    heapq.heappush(hq, (0, x))
    while hq:
        cur_weight, cur_pos = heapq.heappop(hq)
        if cur_weight > dist[cur_pos]:
            continue

        for nxt in graph[cur_pos]:
            nxt_pos, nxt_weight = nxt[0], cur_weight + nxt[1]
            if dist[nxt_pos] > nxt_weight:
                dist[nxt_pos] = nxt_weight
                heapq.heappush(hq, (nxt_weight, nxt_pos))

    for i in range(1, n+1):
        result[i].append(dist[i])


# 파티지점으로부터 다른 지점들까지의 최단 거리 구하기
dijkstra_to_home()

# 최종 판별
answer = 0
for i in range(1, n+1):
    tmp = result[i][0] + result[i][1]
    answer = max(answer, tmp)

print(answer)
