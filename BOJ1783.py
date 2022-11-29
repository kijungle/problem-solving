#221129 1551~1641
#1783_S3 Greedy
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
curx = n
cury = 0
dx = [-2,-1,1,2]
dy = [1,2,2,1]
ans = 1
# 0000
if n == 1:
    ans = 1
if n == 2:
    if m < 3:
        ans = 1
    elif 3 <= m < 5:
        ans = 2
    elif 5 <= m < 7:
        ans = 3
    else:
        ans = 4
if 3 <= n:
    if m <= 6:
        ans = min(4,m)
    else:
        ans = 5 + (m-7)
print(ans)