#221127 1615~1643
#1963_G4
import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
prime = [True] * 10000

def eratosthenes():
    for i in range(2, 100):
        if prime[i]:
            for j in range(2*i, 10000, i):
                prime[j] = False

def bfs(a,b):
    visited = [-1] * 10000
    q = deque()
    q.append(a)
    visited[a] = 0

    while q:
        cur = q.popleft()
        if cur == b:
            return visited[b]
        strCur = str(cur)
        for i in range(4):
            for j in range(10):
                tmp = int(strCur[:i] + str(j) + strCur[i+1:])
                if tmp >= 1000 and visited[tmp] == -1 and prime[tmp]:
                    visited[tmp] = visited[cur] + 1
                    q.append(tmp)
                 
    return 'Impossible'

eratosthenes()
for _ in range(t):
    a, b = map(int, input().split())
    print(bfs(a,b))


# 1 0 3 3
# 1 -> 2~9
# 0 -> 1~9
# 3 -> 1,2 4~9
# 3 -> 1,2 4~9