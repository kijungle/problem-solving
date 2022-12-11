#221211 2134~2156
#17069_G4 DP

import sys
input = sys.stdin.readline

n = int(input())
graph = [[0]+list(map(int, input().split())) for _ in range(n)]
graph.insert(0, [0] * (n+1))
dp = [[[0] * 3 for _ in range(n+1)] for _ in range(n+1)]
# dp[n][n][0], dp[n][n][1], dp[n][n][2]
#dp[n][n] = dp[n-1][n] + dp[n][n-1] + dp[n-1][n-1]
dp[1][2] = [1,0,0]

# 가로, 대각 -> 가로
# 세로, 대각 -> 세로
# 가세대 -> 대각
for i in range(1,n+1):
    for j in range(2,n+1):
        if graph[i][j] == 1:
            continue
        #가로로 오는경우
        if graph[i][j-1] == 0:
            #가->가
            dp[i][j][0] += dp[i][j-1][0]
            #대->가
            dp[i][j][0] += dp[i][j-1][2]

        #세로로 오는경우
        if graph[i-1][j] == 0:
            #세->세
            dp[i][j][1] += dp[i-1][j][1]
            #대->세
            dp[i][j][1] += dp[i-1][j][2]

        #대각으로 오는경우
        if graph[i-1][j-1] == 0 and graph[i][j-1] == 0 and graph[i-1][j] == 0:
            #가->대
            dp[i][j][2] += dp[i-1][j-1][0]
            #세->대
            dp[i][j][2] += dp[i-1][j-1][1]
            #대->대
            dp[i][j][2] += dp[i-1][j-1][2]



print(sum(dp[n][n]))    