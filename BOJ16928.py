#221123 1850~1907
#16928 G5 BFS
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
moveDict = dict()
visited = [False] * 101
for _ in range(n+m):
    s,e = list(map(int, input().split()))
    moveDict[s] = e

def bfs():
    q = deque()
    q.append((1,0))
    visited[1] = True
    
    while q:
        cur, cnt = q.popleft()
        #print(cur)
        if cur == 100:
            return cnt
        if cur in moveDict:
            q.appendleft((moveDict[cur], cnt))
            visited[moveDict[cur]] = True
            continue
        for i in range(1, 7):
            npos = cur + i
            if npos <= 100 and not visited[npos]:
                visited[npos] = True
                q.append((npos, cnt+1))

print(bfs())
# 1->7,94 -> 100