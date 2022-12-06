#221206 2352~0001
#2210_S2 DFS
import sys
input = sys.stdin.readline

graph = [list(map(str, input().split())) for _ in range(5)]
ans = set()
dx = [1,-1,0,0]
dy = [0,0,1,-1]
#Complexity : 25 * dfs
# dfs = 8^5 = 2^20
def dfs(s, depth, x, y):
    if depth == 5:
        ans.add(s)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0<=nx<5 and 0<=ny<5):
            continue
        dfs(s+graph[nx][ny], depth+1, nx, ny)


for i in range(5):
    for j in range(5):
        visited = [[False] * 5 for _ in range(5)]
        visited[i][j] = True
        dfs(graph[i][j], 0, i, j)

print(len(ans))