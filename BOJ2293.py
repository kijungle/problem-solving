#221210 1429~1519
#2293_G5 DP

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
dp = [0] * (10001)
for _ in range(n):
    coin.append(int(input()))

for c in coin:
    if k < c:
        continue
    dp[c] += 1
    for i in range(c+1, k+1):
        dp[i] = dp[i-c] + dp[i]

print(dp[k])