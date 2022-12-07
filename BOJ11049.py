#221207 2009~2041
#11049_G3 DP

import sys
input = sys.stdin.readline

def multiply(a,b):
    return a[0]*a[1]*b[1]

def solve(i,j):
    ret = [1e9, 1e9, 1e9]
    # ii ij, i,i+1/ i+2,j
    for k in range(i,j):
        #print(i,k,'/',k+1,j)
        tmp = multiply(dp[i][k], dp[k+1][j]) + dp[i][k][-1] + dp[k+1][j][-1]
        if ret[-1] > tmp:
            ret[0] = dp[i][k][0]
            ret[1] = dp[k+1][j][1]
            ret[-1] = tmp

    return ret
# n <= 500
n = int(input())
dp = [[[0] * 3 for _ in range(n+1)] for _ in range(n+1)]
matrix = [[0,0]]
for _ in range(n):
    r,c = map(int, input().split())
    matrix.append([r,c])

for i in range(1,n+1):
    r,c = matrix[i]
    dp[i][i][0] = r
    dp[i][i][1] = c

for i in range(1,n):
    cnt = dp[i][i][0] * dp[i][i][1] * dp[i+1][i+1][1]
    r = dp[i][i][0]
    c = dp[i+1][i+1][1]
    dp[i][i+1] = [r,c,cnt]
#O(n^3)
for i in range(n-1, 0, -1):
    for j in range(i+2, n+1):
        #print('solve', i, j)
        dp[i][j] = solve(i,j)

print(dp[1][n][-1])


# 5x3 3x2 2x6
# 5x3x2 + 5x2x6 
# 501 * 501 * 3 
# 12 23 34
# dp[a][b] = a~b 부터 행렬
# dp[1][3] = min(solve(dp[1][1],dp[2][3]), solve(dp[1][2],dp[3][3]))
# dp[n][k] = min(dp[n][n],dp[n+1][k]/dp[n][n+1],dp[n+2][k]/dp[n].../dp[n][k-1]dp[k][k])
# dp[1][1] = solve(matrix[1], matrix[2]) = [5,2]
# dp[2][3] = solve(matrix[2], matrix[3]) = [3,6]
# ans = dp[1][n]
#   0 1 2 3
# 0 0 0 0 0
# 1 0 0 0 0
# 2 0 0 0 0
# 3 0 0 0 0