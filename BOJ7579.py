#221210 1527~1559
#7579_G3

import sys
input = sys.stdin.readline

# 1 <= n <= 100, 1 <= m <= 10,000,000
# app[i] <= 10,000,000 m<=sum(app)
# 0 <= cost[i] <= 100 # sum(cost) <= 10000
n, m = map(int, input().split())
app = [0]+list(map(int, input().split()))
cost = [0]+list(map(int, input().split()))
dp = [[0] * (10001) for _ in range(n+1)]
ans = 1e9

# O(10000N) 
for i in range(1, n+1):
    # 30, 3 / 10, 0 / 20, 3 / 35, 5 / 40, 4
    mem = app[i]
    c = cost[i]
    for j in range(10001):
        if j - c >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c] + mem)
        else:
            dp[i][j] = dp[i-1][j]
        if dp[i][j] >= m:
            ans = min(ans, j)
print(ans)