#221128 1547~1630
#3055_G4 BFS
import sys
from collections import deque
input = sys.stdin.readline
r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
water = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
watered = [[False] * c for _ in range(r)]
visited = [[False] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if graph[i][j] == '*':
            water.append([i,j])
        if graph[i][j] == 'S':
            sx, sy = i, j

def bfs():
    waterQ = deque()
    q = deque()
    q.append([sx,sy,0])
    for x,y in water:
        waterQ.append([x,y])
        watered[x][y] = True
    while q:
        if waterQ:
            p = len(waterQ)
            for _ in range(p):
                x,y = waterQ.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (0<=nx<r and 0<=ny<c):
                        continue
                    if graph[nx][ny] == '.' and not watered[nx][ny]:
                        #print('Water', nx, ny)
                        watered[nx][ny] = True
                        waterQ.append([nx,ny])
        p = len(q)
        for _ in range(p):
            curx, cury, cnt= q.popleft()
            if graph[curx][cury] == 'D':
                return cnt
            for i in range(4):
                nx = curx + dx[i]
                ny = cury + dy[i]
                if not (0<=nx<r and 0<=ny<c):
                    continue
                if not watered[nx][ny] and graph[nx][ny] != 'X' and not visited[nx][ny]:
                    #print('Bieber', nx, ny, cnt+1)
                    q.append([nx,ny,cnt+1])
                    visited[nx][ny] = True
    return 'KAKTUS'

# for i in range(r):
#     print(*graph[i])
print(bfs())
# for i in range(r):
#     print(*watered[i])
        
        


    
