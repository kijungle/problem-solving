#221206 1832~1849
#11660_S1 Prefix Sum

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
prefixSum = [[0] * (n+1) for _ in range(n+1)]
ans = []

for i in range(n):
    for j in range(n):
        prefixSum[i+1][j+1] = prefixSum[i+1][j] + graph[i][j]
#O(m + n*2)
for _ in range(m):
    tmp = 0
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(x1, x2+1):
        tmp += prefixSum[i][y2] - prefixSum[i][y1-1]
    ans.append(tmp)

for i in ans:
    print(i)