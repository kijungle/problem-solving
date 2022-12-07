#221207
#1655_G2 HeapQ

import sys
import heapq
input = sys.stdin.readline

n = int(input()) 
# left right
# 1 [-1] [] -> 1
# 2 [-1] [2] -> 1
# 3 [-3,-1] [2] -> 3
# 4 [-2,-1] > [3,4] -> 2
# 5 [-3,-2,-1] [5,4] -> 3
leftHeap = []
rightHeap = []
ans = []
for _ in range(n):
    k = int(input())
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -k)
    else:
        heapq.heappush(rightHeap, k)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        rightValue = heapq.heappop(rightHeap)
        leftValue = heapq.heappop(leftHeap)

        heapq.heappush(rightHeap, -leftValue)
        heapq.heappush(leftHeap, -rightValue)
    

    print(-leftHeap[0])

