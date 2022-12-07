#221207 2054~2137
#25682_G5 DP
import sys
input = sys.stdin.readline

def solve(color):
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            # Color 랑 같아아함
            if (i+j) % 2 == 0:
                if graph[i][j] == color:
                    tmp = 0
                else:
                    tmp = 1
            # 달라야함
            else:
                if graph[i][j] != color:
                    tmp = 0
                else:
                    tmp = 1
            dp[i+1][j+1] = dp[i+1][j] + tmp
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] += dp[i-1][j]
    
    minCount = 1e9
    for i in range(n-k+1):
        for j in range(m-k+1):
            sx, sy = i, j
            ex, ey = i+k, j+k
            cnt = dp[ex][ey] - dp[ex][sy] - dp[sx][ey] + dp[sx][sy]
            minCount = min(cnt, minCount)
    
    return minCount


#dp[n][k] = 1,1 ~ n,k 까지 색칠
# 필요한 색칠수 = dp[n][k] + dp[1][1] - dp[n][1] - dp[1][k]


n,m,k = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
print(min(solve('B'), solve('W')))