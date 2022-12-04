#221204 2320~2347
#1300_G2 Parametric Search(Binary Search)

import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
s, e = 1, k # 1,7 mid = 4(6) -> 5,7 6(8) -> 5 5 5(6)

while s <= e:
    mid = (s+e) // 2
    print(mid)
    tmp = 0
    for i in range(1, n+1):
        tmp += min(mid//i, n) 
    if tmp >= k:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1
print(ans)