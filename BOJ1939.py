#221203 1947~2011
#1939_G3 Dijkstra
import sys
import heapq
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
ans = 0
dist = [1e10] * (n+1)
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((-c,b))
    graph[b].append((-c,a))
s,e = map(int, input().split())

def bfs(s):
    q = []
    heapq.heappush(q, [0,s])
    dist[s] = 0
    # 0,1 -> -3, 3 -> -3, 1

    while q:
        cost, cur = heapq.heappop(q)
        if dist[cur] < cost:
            continue
        for w, npos in graph[cur]:
            if cost != 0:
                nw = max(cost, w)
                if nw > 0:
                    nw *= -1
            else:
                nw = w
            #print(cur, npos, cost, nw)
            if nw < dist[npos]:
                dist[npos] = nw
                heapq.heappush(q,[nw,npos])

bfs(s)
print(abs(dist[e]))

# 1 -> 3 -> 1 -> 2 -> 3
# 1(0) -> 3(-3) -> 1(-3) -> 2(-2) -> 3(-3)
            


