#221202 1738~1759
#2565_G5 DP
import sys
input = sys.stdin.readline
n = int(input())
line = []
ans = 1e9
dp = [1] * n

for _ in range(n):
    a,b = map(int, input().split())
    line.append((a,b))
line.sort(key = lambda x : x[0])

for i in range(1, n):
    for j in range(0, i):
        if line[j][1] < line[i][1]:
            dp[i] = max(dp[j]+1, dp[i])

print(n - max(dp))
# 8 2 9 1 4 6 7 5
# 1 1 2 1 2 3 4 3