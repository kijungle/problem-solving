#221210 1600~1636
#15683_G4 Brute Force
import sys
from copy import deepcopy
input = sys.stdin.readline
# 1 <= n,m <= 8
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 1e9
cctv = []
# 북 동 남 서 순 0,1,2,3
dx = [-1,0,1,0]
dy = [0,1,0,-1]
mode = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,3],[0,1,2],[1,2,3],[2,3,0]],
    [[0,1,2,3]]
]
#depth < 8 (cctv)
for i in range(n):
    for j in range(m):
        if 1 <= graph[i][j] <= 5:
            cctv.append((graph[i][j],i,j))
#2^9
def getArea(graph):
    for i in range(len(cctv)):
        x,y = cctv[i][1], cctv[i][2]
        modeNum = graph[x][y] % 10
        num = graph[x][y] // 10
        #print(num, modeNum)
        for dir in mode[num][modeNum]:
            nx, ny = x+dx[dir], y+dy[dir]
            while 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 6:
                    break
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 7
                nx, ny = nx + dx[dir], ny + dy[dir]
    ret = 0
    for i in range(n):
        ret += graph[i].count(0)
    return ret
# 4^8 = 2^16
def dfs(idx, graph):
    global ans
    if idx == len(cctv):
        ans = min(ans, getArea(graph))
        return
        
    cctvNum = cctv[idx][0]
    x,y = cctv[idx][1], cctv[idx][2]
    for m in range(len(mode[cctvNum])):
        newGraph = deepcopy(graph)
        newGraph[x][y] = cctvNum * 10 + m
        dfs(idx+1, newGraph)
dfs(0, graph)
print(ans)