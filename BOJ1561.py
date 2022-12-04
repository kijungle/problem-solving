#221204 2352~0021
#1561_G2 Parametric Search
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))

if n < m:
    print(n)
    sys.exit()
s, e = 0, 6*1e10

while s <= e:
    mid = (s+e) // 2
    cnt = m
    for i in range(m):
        cnt += mid // arr[i] # mid =
    if cnt >= n:
        t = mid
        e = mid - 1
    else:
        s = mid + 1

total = m
for i in range(m):
    total += (t-1) // arr[i]

for i in range(m):
    if t % arr[i] == 0:
        total += 1
    if total == n:
        print(i+1)
        break