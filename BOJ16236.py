#221127 1537~1600
#16236_G3 BFS
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            sx, sy = i, j

def bfs(size,sx,sy):
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((sx,sy))
    visited[sx][sy] = 0
    fishList = []
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if visited[nx][ny] != -1:
                continue
            if size < graph[nx][ny]:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx,ny))
            if 1 <= graph[nx][ny] <= size:
                fishList.append((visited[nx][ny], graph[nx][ny], nx, ny))

    return fishList

def canEatFish(size):
    for i in range(n):
        for j in range(n):
            if 1 <= graph[i][j] < size:
                return True
    return False

    

def solve():
    global sx, sy
    size = 2
    exp = 0
    ans = 0

    while canEatFish(size):
        flag = False
        #distance, size, x, y
        fishList = bfs(size, sx, sy)
        fishList.sort(key = lambda x: (x[0], x[2], x[3]))
        #print(fishList)
        for fish in fishList:
            if fish[1] < size:
                ans += fish[0]
                exp += 1
                sx = fish[2]
                sy = fish[3]
                graph[fish[2]][fish[3]] = 0
                flag = True

                if exp == size:
                    exp = 0
                    size += 1
                break
        if not flag:
            break
    return ans


print(solve())