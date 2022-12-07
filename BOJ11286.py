#221207 1802~1805
#11286_S1 heap

import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    k = int(input())
    if k == 0:
        if q:
            num,sign = heapq.heappop(q)
            print(num * sign)
        else:
            print('0')
    else:
        if k < 0:
            heapq.heappush(q, (abs(k), -1))
        else:
            heapq.heappush(q, (abs(k), 1))

