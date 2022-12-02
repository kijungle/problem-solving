#221202 1924~1945
#2110_G4 binary Search
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
dist = [1e9+1] * n
ans = -1
for _ in range(n):
    house.append(int(input()))
house.sort()
start = 1
end = house[-1] - house[0]

def bSearch(s,e):
    global ans
    if s > e:
        return

    mid = (s+e) // 2
    prev = house[0]
    count = 1
    for i in range(len(house)):
        if house[i] - prev >= mid:
            count += 1
            prev = house[i]
    if count >= c:
        ans = max(ans, mid)
        bSearch(mid+1, e)
    else:
        bSearch(s, mid-1)
        

if c == 2:
    print(end)
else:
    bSearch(start, end)
    print(ans)
# 1 2 . 4 . . . 8 9
# 1     0       1