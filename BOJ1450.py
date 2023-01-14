#230114 1536~1603
#1450_G1 Binary Search & Meet-in-the-middle
import sys
from itertools import combinations
input = sys.stdin.readline

# n <= 30, c <= 1e9
n, c = map(int, input().split())
arr = list(map(int, input().split())) # size = n
subArr1 = arr[:n//2]
subArr2 = arr[n//2:]
subSum1 = []
subSum2 = []
ans = 0

# 2^16
for i in range(len(subArr1)+1):
    for com in combinations(subArr1,i):
        subSum1.append(sum(com))

for i in range(len(subArr2)+1):
    for com in combinations(subArr2,i):
        subSum2.append(sum(com))

#print(subSum1, subSum2)
subSum1.sort()
for s in subSum2:
    if s > c:
        continue
    
    start = 0
    end = len(subSum1) - 1
    while start <= end:
        mid = (start+end)//2
        if subSum1[mid] + s > c:
            end = mid - 1
        else:
            start = mid + 1
    ans += end + 1

print(ans)