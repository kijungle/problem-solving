#230111 1625~1635
#1956_G4
import sys
input = sys.stdin.readline

# 64000000
# v <= 400, e <= 160000
v,e = map(int, input().split())
dist = [[1e9] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    if dist[a][b] > c:
        dist[a][b] = c

for m in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            dist[i][j] = min(dist[i][j], dist[i][m] + dist[m][j])

ans = 1e9
for i in range(1, v+1):
    ans = min(ans, dist[i][i])

print(-1 if ans == 1e9 else ans)