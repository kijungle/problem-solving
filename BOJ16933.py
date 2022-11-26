#221126 1539~1617
#Gold 1 BFS
import sys
from collections import deque
n,m,k = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[False] * (k+1) for _ in range(m)] for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs():
    q = deque()
    q.append((0,0,0,1))
    visited[0][0][0] = True

    while q:
        p = len(q)
        for _ in range(p):
            x,y,cnt,day = q.popleft()
            if x == n-1 and y == m-1:
                return day
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0<=nx<n and 0<=ny<m):
                    continue
                if graph[nx][ny] == 0 and not visited[nx][ny][cnt]:
                    visited[nx][ny][cnt] = True
                    q.append((nx,ny,cnt,day+1))
                elif graph[nx][ny] == 1 and cnt < k and not visited[nx][ny][cnt+1]:
                    #night
                    if day % 2 == 0:
                        q.append((x,y,cnt,day+1))
                    else:
                        visited[nx][ny][cnt+1] = True
                        q.append((nx,ny,cnt+1,day+1))
    return -1

print(bfs())