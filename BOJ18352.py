#221126 2018~2029
#18352 Silver 2 Dijkstra
import sys
import heapq
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
dist = [1e9] * (n+1)
graph = [[] for _ in range(n+1)]
flag = False
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dijkstra(x):
    q = []
    dist[x] = 0
    for npos in graph[x]:
        heapq.heappush(q, (1,npos))

    while q:
        #print(q)
        cost, cur = heapq.heappop(q)
        #print(cur)
        if cost <= dist[cur]:
            dist[cur] = cost
            for npos in graph[cur]:
                heapq.heappush(q, (cost+1, npos))


dijkstra(x)
for i in range(1, n+1):
    if dist[i] == k:
        flag = True
        print(i)
if not flag:
    print('-1')