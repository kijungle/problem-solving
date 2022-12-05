#221205 1808~1835
#12865_G5 DP(knapsack)

import sys
input = sys.stdin.readline

n,k = map(int, input().split())
arr = [(0,0)]
dp = [[0] * (k+1) for _ in range(n+1)]
for _ in range(n):
    w, v = map(int, input().split())
    arr.append((w,v))

for i in range(1, n+1):
    for j in range(1, k+1):
        w,v = arr[i][0], arr[i][1]
        if w <= j:
            #이번 물건 넣는경우 , 안넣는경우
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
        else:
            #이번 물건을 안넣었을때 최댓값 을 넣어줌
            dp[i][j] = dp[i-1][j]
# .       1 2 3 4 5 6 7
# 0       0 0 0 0 0 0  0
# 1 6 13  0 0 0 0 0 13 13
# 2 4 8 . 0 0 0 8 8 13 13
# 3 3 6   0 0 6 8 8 13 14 (6+8, 13)
# 4 5 12  0 0 6 8 12 13 14
print(dp[n][k])