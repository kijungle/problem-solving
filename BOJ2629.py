#221208 1600~1648
#2629_G3 DP
import sys
input = sys.stdin.readline

n = int(input()) # n <= 30
stone = [0]+list(map(int, input().split()))
m = int(input()) # m <= 7
marble = list(map(int, input().split()))
ans = []
# 40001 * 7 = 280000 * (int)
dp = [[0 for _ in range(40001)] for _ in range(n+1)]

#dp[n][k] = 1 -> n개의 Stone으로 k를 만들수있음
#O(40000N)
for i in range(1, n+1):
    cur = stone[i]
    dp[i][cur] = 1
    for w in range(1, 40001):
        if dp[i-1][w] == 1:
            dp[i][w] = 1
            if w+cur <= 40000:
                dp[i][w+cur] = 1
            if 1 <= w-cur <= 40000:
                dp[i][w-cur] = 1
            if 1 <= cur-w <= 40000:
                dp[i][cur-w] = 1

for i in range(m):
    cur = marble[i]
    if dp[n][cur] == 1:
        ans.append('Y')
    else:
        ans.append('N')

print(*ans)
