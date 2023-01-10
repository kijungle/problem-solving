#230110 1351~1433
#9370 G2 Dijkstra
import sys
import heapq
input = sys.stdin.readline

c = int(input())
# c <= 100
# O(C * 3MlogN)

#Dijkstra O(ElogV)
def solve(dist, s):
    q = []
    dist[s] = 0
    heapq.heappush(q,(0,s))

    while q:
        cost, cur = heapq.heappop(q)
        if dist[cur] < cost:
            continue
        for w, npos in graph[cur]:
            nw = cost + w
            if nw < dist[npos]:
                dist[npos] = nw
                heapq.heappush(q, (nw, npos))
#O(1)
def check(x, g, h, res):
    # d1 : s->g->h->x
    d1 = dist[g] + distG[h] + distH[x]
    # d2 : s->h->g->x
    d2 = dist[h] + distH[g] + distG[x]
    if res == min(d1,d2):
        return True
    return False

for _ in range(c):
    ans = []
    #n = 교차로(2000), m = 도로(50000), t = 후보(100)
    n,m,t = map(int, input().split())
    dist = [1e9] * (n+1)
    distG = [1e9] * (n+1)
    distH = [1e9] * (n+1)
    graph = [[] for _ in range(n+1)]
    #s = 출발지
    s,g,h = map(int, input().split())
    #a<->b 길이 d
    for _ in range(m):
        a,b,d = map(int, input().split())
        graph[a].append((d,b))
        graph[b].append((d,a))
    solve(dist, s)
    solve(distG, g)
    solve(distH, h)

    #t개의 목적지 후보들 t_n != s
    for _ in range(t):
        x = int(input())
        if check(x, g, h, dist[x]):
            ans.append(x)
        
    ans.sort()
    print(*ans)
    # s -> (g<->h) -> x
