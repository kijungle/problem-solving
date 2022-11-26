#221126 2225~2242
#1238 Gold 3 Dijkstra
import sys
import heapq
input = sys.stdin.readline
n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,t = map(int, input().split())
    graph[a].append((b,t))

def dijkstra(start):
    q = []
    dist = [1e9] * (n+1)
    dist[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        cost, cur = heapq.heappop(q)
        if dist[cur] < cost:
            continue
        for npos, w in graph[cur]:
            nw = w + cost
            if nw < dist[npos]:
                dist[npos] = nw
                heapq.heappush(q, (nw, npos))
    return dist
ans = 0
for i in range(1,n+1):
    goToX = dijkstra(i)
    goToHome = dijkstra(x)
    ans = max(ans, goToX[x] + goToHome[i])
print(ans)
    
