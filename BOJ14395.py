#221127 1657~1712
#14395_G5 BFS
import sys
from collections import deque
input = sys.stdin.readline
s, t = map(int, input().split())
visited = set()
def bfs(s, t):
    q = deque()
    q.append((s,''))
    visited.add(s)

    while q:
        cur, op = q.popleft()
        if cur > 1e9:
            continue
        #print(q)
        #print(visited)
        if cur == t:
            return op
        for i in range(4):
            if i == 0:
                ns = cur*cur
                if ns not in visited:
                    visited.add(ns)
                    q.append((ns,op+'*'))
            elif i == 1:
                ns = cur+cur
                if ns not in visited:
                    visited.add(ns)
                    q.append((ns,op+'+'))
            elif i == 2:
                ns = cur-cur
                if ns != 0 and ns not in visited:
                    visited.add(ns)
                    q.append((ns,op+'-'))
            elif i == 3:
                if s == 0:
                    continue
                ns = cur // cur
                if ns not in visited:
                    visited.add(ns)
                    q.append((ns,op+'/'))
    return -1

if s == t:
    print('0')
else:
    print(bfs(s,t))
