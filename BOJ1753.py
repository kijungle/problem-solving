#221126 2032~2055
#1753 Gold 4 Dijkstra
import sys
import heapq
input = sys.stdin.readline
v,e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
dist = [1e9] * (v+1)
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))


def dijkstra(s):
    q = []
    dist[s] = 0
    heapq.heappush(q, (0,s))
    
    while q:
        cost, cur = heapq.heappop(q)
        if dist[cur] < cost:
            continue
        for npos, w in graph[cur]:
            nw = cost + w
            if nw < dist[npos]:
                dist[npos] = nw
                heapq.heappush(q, (nw, npos))

#print(start)
dijkstra(start)
for i in range(1, v+1):
    print('INF') if dist[i] == 1e9 else print(dist[i])
