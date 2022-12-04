#221205 0134~0154
#2981_G4 Math

import sys
from math import sqrt
input = sys.stdin.readline
n = int(input())
arr = []
diff = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
for i in range(1, n):
    diff.append(arr[i] - arr[i-1])

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

tmp = diff[0]
for i in range(1, len(diff)):
    _min, _max = min(tmp, diff[i]), max(tmp, diff[i])
    tmp = gcd(_min, _max)
for i in range(2, tmp+1):
    if tmp % i == 0:
        print(i, end = ' ')

    # 6 34 38
    # 4 32 36
    # 4 13 16 22 82
# n1 % m == n2 % m == n3 % m
# 1 < m <= n1 if n1 <= 10억
