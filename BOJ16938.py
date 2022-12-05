#221205 1744~1750
#16938_G5 Brute Force

import sys
from itertools import combinations
input = sys.stdin.readline

n,l,r,x = map(int, input().split())
arr = list(map(int, input().split()))
_sum = 0
# 15C2 + 15C3 ... + 15C15 = 2^15
# O(2^n)
ans = 0
for i in range(2,n+1):
    candidates = list(combinations(arr,i))
    for candidate in candidates:
        mx = max(candidate)
        mn = min(candidate)
        if (mx-mn) < x:
            continue
        if l <= sum(candidate) <= r:
            ans += 1

print(ans)
