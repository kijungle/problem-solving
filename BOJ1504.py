#221211 2251~2318
#1504_G4 Dijkstra

import sys
import heapq
input = sys.stdin.readline


n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
dist = [1e9] * (n+1)
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
u, v = map(int ,input().split())
q = []
for cost, npos in graph[1]:
    heapq.heappush(q, (cost, npos))

#O(ElgE)
def dijkstra(start, end):
    dist = [1e9] * (n+1)
    q = []
    heapq.heappush(q, (0,start))
    dist[start] = 0
    # 0,start -> 1, 2 / 2, 4
    while q:
        # start -> cur : cost
        cost, cur = heapq.heappop(q)
        if dist[cur] < cost:
            continue
        for w, npos in graph[cur]:
            nw = w + cost
            if nw < dist[npos]:
                dist[npos] = nw
                heapq.heappush(q, (nw, npos))

    return dist[end]

            
def getDist(start, end, u, v):
    # 1->u->v->end # Dijkstra 총 6번 실행
    # 1->v->u->end
    # 둘중 최솟값 찾기
    dist1 = dijkstra(start,u) + dijkstra(u,v) + dijkstra(v,end)
    dist2 = dijkstra(start,v) + dijkstra(v,u) + dijkstra(u,end)
    if dist1 >= 1e9 and dist2 >= 1e9:
        return -1
    else:
        return min(dist1, dist2)

print(getDist(1,n,u,v))