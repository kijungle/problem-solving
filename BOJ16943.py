#221205 2308~2314
#16943_S1 BruteForce
import sys
from itertools import permutations
input = sys.stdin.readline

a, b = map(int, input().split())
arr = list(str(a))
digit = 10 ** (len(arr) - 1)
ans = -1
candidates = list(permutations(arr, len(arr)))

for candidate in candidates:
    tmp = ''
    for ch in candidate:
        tmp += ch
    num = int(tmp)
    if num < b and digit <= num:
        ans = max(ans, num)

print(ans)