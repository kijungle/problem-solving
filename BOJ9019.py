#221123 1909~1946
#9019 G4 BFS
import sys
input = sys.stdin.readline
from collections import deque
def operateD(num):
    return (num * 2) % 10000

def operateS(num):
    if num == 0:
        return 9999
    else:
        return num-1

def operateL(num):
    # 0001 -> 1000
    # 1234 -> 2341
    x1 = num // 1000 # 0
    x2 = (num % 1000) // 100 # 0
    x3 = (num % 100) // 10 # 0
    x4 = num % 10 # 1
    return x2 * 1000 + x3 * 100 + x4 * 10 + x1

def operateR(num):
    x1 = num // 1000 # 0
    x2 = (num % 1000) // 100 # 0
    x3 = (num % 100) // 10 # 0
    x4 = num % 10 # 1
    return x4 * 1000 + x1 * 100 + x2 * 10 + x3
    
def bfs(a,b):
    q = deque()
    q.append(a)
    visited[a] = ''
    while q:
        cur = q.popleft()
        if cur == b:
            return visited[b]
        npos = operateD(cur)
        if visited[npos] == False:
            visited[npos] = visited[cur] + 'D'
            q.append((npos))
        npos = operateS(cur)
        if visited[npos] == False:
            visited[npos] = visited[cur] + 'S'
            q.append((npos))
        npos = operateL(cur)
        if visited[npos] == False:
            visited[npos] = visited[cur] + 'L'
            q.append((npos))
        npos = operateR(cur)
        if visited[npos] == False:
            visited[npos] = visited[cur] + 'R'
            q.append((npos))
    
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    visited = [False] * 10001
    print(bfs(a,b))