#221211 2234~2250
#7569_G5 BFS

import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = []
ans = -1
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
q = deque()
visited = [[[False] * m for _ in range(n)] for _ in range(h)]
dist = [[[0] * m for _ in range(n)] for _ in range(h)]
for _ in range(h):
    graph.append([list(map(int, input().split())) for _ in range(n)])

for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                q.append([k,i,j])

def bfs():
    while q:
        z,x,y = q.popleft()
        visited[z][x][y] = True
        for i in range(6):
            nx,ny,nz = x+dx[i],y+dy[i],z+dz[i]
            if not (0 <= nx < n and 0 <= ny < m and 0 <= nz < h):
                continue
            if graph[nz][nx][ny] == 0 and not visited[nz][nx][ny]:
                q.append([nz,nx,ny])
                graph[nz][nx][ny] = 1
                dist[nz][nx][ny] = dist[z][x][y] + 1
                visited[nz][nx][ny] = True

bfs()
flag = True
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0:
                flag = False
                break

if not flag:
    print(-1)
    sys.exit()

for k in range(h):
    for i in range(n):
        for j in range(m):
            ans = max(ans, dist[k][i][j])

print(ans)


