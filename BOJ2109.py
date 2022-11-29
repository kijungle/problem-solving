#221129 1852~1938
#2109_G3 heapq/Greedy
import sys
import heapq
input = sys.stdin.readline
n = int(input())
courseList = []
ans = 0
candidate = []
for _ in range(n):
    pay, day = map(int, input().split())
    heapq.heappush(courseList, (-day, -pay))

for i in range(10000, 0, -1):
    while courseList:
        if i <= abs(courseList[0][0]):
            heapq.heappush(candidate, heapq.heappop(courseList)[1])
        else:
            break
    if candidate:
        ans += heapq.heappop(candidate)

print(-ans)