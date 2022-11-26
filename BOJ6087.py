#221126 2243~2255
#6087_G3 Dijkstra
import sys
import heapq
input = sys.stdin.readline

w, h = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(h)]
dist = [[1e9] * w for _ in range(h)]
goal = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(h):
    for j in range(w):
        if graph[i][j] == 'C':
            goal.append((i,j))

def dijkstra(pos):
    x = pos[0]
    y = pos[1]
    q = []
    dist[x][y] = 0
    heapq.heappush(q, (0,x,y,-1))

    while q:
        cost, curx, cury, dir = heapq.heappop(q)
        if dist[curx][cury] < cost:
            continue
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]
            if not (0<=nx<h and 0<=ny<w):
                continue
            if graph[nx][ny] == '*':
                continue
            #First Move
            if dir == -1:
                nw = cost
                if nw <= dist[nx][ny]:
                    dist[nx][ny] = nw
                    heapq.heappush(q, (nw, nx, ny, i))
            # Same Direction
            elif dir != -1 and dir == i:
                nw = cost 
                if nw <= dist[nx][ny]:
                    dist[nx][ny] = nw
                    heapq.heappush(q, (nw, nx, ny, i))
            # Not Same Direction
            elif dir != -1 and dir != i:
                nw = cost + 1
                if nw <= dist[nx][ny]:
                    dist[nx][ny] = nw
                    heapq.heappush(q, (nw, nx, ny, i))




dijkstra(goal[0])
print(dist[goal[1][0]][goal[1][1]])