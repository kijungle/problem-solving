#221207 1757~1801
#11279_S2 heapq

import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    k = int(input())
    if k == 0:
        if q:
            _max = heapq.heappop(q)
            print(abs(_max))
        else:
            print(0)
    else:
        heapq.heappush(q, -k)


