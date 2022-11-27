#221127 1644~1656
#10026_G5 DFS
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = [[False] * n for _ in range(n)]
ans = []

def dfs(x, y):
    visited[x][y] = True
    cur = graph[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0<=nx<n and 0<=ny<n):
            continue
        if visited[nx][ny]:
            continue
        if graph[nx][ny] == cur:
            dfs(nx,ny)

    
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            cnt += 1
ans.append(cnt)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
visited = [[False] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            cnt += 1
ans.append(cnt)
print(ans[0],ans[1])