# 221202 1902~1914
#1654_S2 Binary Search

import sys
input = sys.stdin.readline
k, n = map(int, input().split())
line = []
ans = -1

for _ in range(k):
    line.append(int(input()))

def bSearch(s, e):
    global ans
    if s > e:
        return 
    mid = (s+e) // 2
    count = 0
    for i in range(len(line)):
        count += line[i] // mid
    if count < n:
        bSearch(s, mid-1)
    else:
        ans = max(ans, mid)
        bSearch(mid+1, e)
 
bSearch(1, max(line))
print(ans)