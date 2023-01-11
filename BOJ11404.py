#230111 1614~1623
#11404_G4 Floyd-Warshall
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
dist = [[1e9] * (n+1) for _ in range(n+1)]
edges = []
for i in range(1,n+1):
    dist[i][i] = 0

for _ in range(m):
    a,b,c = map(int, input().split())
    if dist[a][b] > c:
        dist[a][b] = c


for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == 0 or dist[i][j] == 1e9:
            print('0', end = ' ')
        else:
            print(dist[i][j], end = ' ')
    print()