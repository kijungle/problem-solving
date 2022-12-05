#221205 1751~1807
#9251_G5 DP

import sys
input = sys.stdin.readline
str1 = input().rstrip()
str2 = input().rstrip()
dp = [[0] * (len(str2)+1) for _ in range(len(str1)+1)]

#O(n2) 1,000,000
for i in range(1, len(str1)+1):
    subString = str1[:i]
    for j in range(1, len(str2)+1):
        compare = str2[:j]
        if subString[-1] == compare[-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(str1)][len(str2)])
# acaykp , capcak
#     acaykp -> c/ca/cap/capc/capca/cpacak
#   0 1 2 3 4 5 6
# 0 0 0 0 0 0 0 0
# 1 0 0 1 1 1 1 1
# 2 0 1 1 1 2 2 2
# 3 0 1 2 2 2 3 3
# 4 0 1 2 2 2 3 3
# 5 0 1 2 2 2 3 4
# 6 0 1 2 3 3 3 4