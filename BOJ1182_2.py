#221127 1801~1809
#1182_S2 BitMasking
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
bit = (1 << n) # n =5 100000 1 ~ 11111
ans = 0 
for i in range(1, bit):
    _sum = 0
    for j in range(n):
        # 10101 & 1 = 1
        # 10101 & 10 = 0
        # 10101 & 100 = 1
        if (i & (1 << j)):
            _sum += arr[j]
    if _sum == s:
        ans += 1

print(ans)