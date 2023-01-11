#230111 1544~1610
#11657_G4 Bellman-Ford
import sys
input = sys.stdin.readline


# O(VE)
# n = vertex (500), m = edge (6000)
n, m = map(int,input().split())
edges = []
dist = [1e9] * (n+1)
for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append([a,b,c])


def bellmanFord(s):
    dist[s] = 0
    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            npos = edges[j][1]
            cost = edges[j][2]

            if dist[cur] != 1e9 and dist[npos] > dist[cur] + cost:
                dist[npos] = dist[cur] + cost

                if i == n-1:
                    return True
        #print(i, dist)
    return False

cycle = bellmanFord(1)
if cycle:
    print('-1')
else:
    for i in range(2, n+1):
        if dist[i] != 1e9:
            print(dist[i])
        else:
            print('-1')
