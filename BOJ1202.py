#221129 1801~1851
#1202_G2
import sys
import heapq
input = sys.stdin.readline

n,k = map(int, input().split())
gemList = [list(map(int, input().split())) for _ in range(n)]
bagList = [int(input()) for _ in range(k)]
gemList.sort()
bagList.sort()
ans = 0
candidate = []

for bag in bagList:
    while gemList:
        #print(gemList)
        if gemList[0][0] <= bag:
            weight, cost = heapq.heappop(gemList)
            heapq.heappush(candidate, -cost)
        else:
            break
    
    if candidate:
        ans += abs(heapq.heappop(candidate))

   
print(ans)