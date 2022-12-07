#221207 1855~2002
#11066_G3 DP
import sys
input = sys.stdin.readline
t = int(input())
cnt = 0

# k <= 500
#O(k)
def solve(i,j):
    ret = 1e9
    for p in range(i,j):
        ret = min(ret, dp[i][p] + dp[p+1][j])
    ret += sum(novel[i:j+1])

    return ret

for _ in range(t):
    k = int(input())
    novel = [0]+list(map(int, input().split()))
    dp = [[0 for _ in range(k+1)] for _ in range(k+1)]
    
    for i in range(1, k+1):
        for j in range(1, k+1):
            if i+1 == j:
                dp[i][j] = novel[i] + novel[j]
    #O(k^3)
    for i in range(k-1, 0, -1):
        for j in range(i+1, k+1):
            if dp[i][j] != 0: continue
            dp[i][j] = solve(i,j)
            
    print(dp[1][k])

#dp[n][k] = n번 부터 k까지 파일 을 합친것
#dp[n][k] = sum(novel [i~j]) + min(dp[n][n] + dp[n+1][k]
# dp[n][n+1] + dp[n+2][k],) = min(dp[i][p] + dp[p+1][j] p in range(i,j))
# i <= p < p+1 <= j
# dp[2][4] = 1개씩 합친것/.. 2,3
# dp[2][3] + dp[4][4], 
# dp[2][2] + dp[3][4]