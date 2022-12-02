#221202 1914~1922
#2805_S2 Binary Search

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
ans = -1

def bSearch(s, e):
    global ans
    if s > e:
        return
    mid = (s+e) // 2
    count = 0
    for i in range(n):
        if mid >= trees[i]:
            continue
        count += (trees[i] - mid)
    if count < m:
        bSearch(s, mid-1)
    if count >= m:
        ans = max(ans, mid)
        bSearch(mid+1, e)

bSearch(0, max(trees))
print(ans)
# 10 15 17 20
# 1 ~ 20 10 10+5+0+7 = 27