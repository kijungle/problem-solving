#221208 1431~1528
#1520_G3 DFS+DP

import sys
input = sys.stdin.readline


dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x,y):
    if x == n-1 and y == m-1:
        return 1
    #-1 -> 탐색
    if dp[x][y] == -1:
        dp[x][y] = 0
    
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not (0<=nx<n and 0<=ny<m):
                continue
            if graph[x][y] > graph[nx][ny]:
                dp[x][y] += dfs(nx,ny)
    
    return dp[x][y]
# 0,0 -> 1,0 / 0,1
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
print(dfs(0,0))

for i in range(n):
    print(*dp[i])
# 0 1 0 0 0
# 1 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 
# dp[n][k] = 경로의 수 (0,0) ~ (n,k)
# dp[n][k] = dp[n-1][k] dp[n][k-1] 중 하나를 받아야ㅐ함
# dp[n][k] = if dp[n-1][k] > dp[n][k] : dp[n][k]
