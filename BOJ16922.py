#221202 1600~1611
#16922_S3 combination & brute force
import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline
n = int(input())
canMake = [False] * 1001
ans = 0
numbers = combinations_with_replacement('ivxl', n)
for num in numbers:
    total = 0
    for i in range(n):
        if num[i] == 'i':
            total += 1
        elif num[i] == 'v':
            total += 5
        elif num[i] == 'x':
            total += 10
        elif num[i] == 'l':
            total += 50
    #print(total)
    canMake[total] = True

for i in range(1, 1001):
    if canMake[i]:
        ans += 1

print(ans)
#n=1 i v x l
#n=2 ii iv ix il / vi vv vx vl / xi xv xx xl / li lv lx ll

# 50 * 20 = 1000