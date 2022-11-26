#221126 2102~2107
#1916 Gold 5 Dijkstra
import sys
import heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
dist = [1e9] * (n+1)
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
s,e = map(int, input().split())

def dijkstra(s,e):
    q = []
    heapq.heappush(q, (0,s))
    dist[s] = 0

    while q:
        cost, cur = heapq.heappop(q)
        if dist[cur] < cost:
            continue
        for npos, w in graph[cur]:
            nw = w + cost
            if nw < dist[npos]:
                dist[npos] = nw
                heapq.heappush(q, (nw, npos))


dijkstra(s,e)
print(dist[e])