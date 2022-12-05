#221205 1705~1738
#16937_S3 Brute Force + Math
import sys
from itertools import permutations
input = sys.stdin.readline
h,w = map(int, input().split())
graph = [[0] * w for _ in range(h)]
n = int(input())
arr = []
ans = 0

for _ in range(n):
    r,c = map(int, input().split())
    arr.append((r,c)) #Not Rotate

stickers = list(permutations(arr,2))

def putSticker(a,b):
    w1, h1 = max(a[1],b[1]), a[0]+b[0]
    w2, h2 = a[1]+b[1], max(a[0],b[0])
    if w1 <= w and h1 <= h:
        return a[0]*a[1] + b[0]*b[1]
    if w2 <= w and h2 <= h:
        return a[0]*a[1] + b[0]*b[1]
    return 0

# 100P2 * 4 = 20000
for a,b in stickers:
    rotateA = (a[1],a[0])
    rotateB = (b[1],b[0])
    ans = max(ans, putSticker(a,b))
    ans = max(ans, putSticker(rotateA, b))
    ans = max(ans, putSticker(a, rotateB))
    ans = max(ans, putSticker(rotateA, rotateB))
print(ans)

#100C2
# 2 3 + 1 1  = 3 3 or 2 4
# 5 10 + 1 1 = 5 11 or 6 10
# 1 2 + 2 1 = 3 2 or 2 3 or 2 2
# 5 10 + 2 3 = 7 10 or 5 13