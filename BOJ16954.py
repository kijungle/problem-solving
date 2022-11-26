#221126 1638~1703
#16954 Gold 3 BFS
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
graph = [list(input().rstrip()) for _ in range(8)]
dx = [-1,-1,-1,0,0,0,1,1,1]
dy = [-1,0,1,-1,0,1,-1,0,1]
def moveGraph(graph):
    newGraph = deepcopy(graph)
    newGraph.pop()
    newGraph.insert(0, ['.','.','.','.','.','.','.','.'])
    return newGraph

def bfs(graph):
    q = deque()
    q.append((7,0,1))
    
    while q:
        p = len(q)
        for _ in range(p):
            x,y,cnt = q.popleft()
            if graph[x][y] == '#':
                continue
            if cnt >= 8:
                return 1
            for i in range(9):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0 <= nx < 8 and 0 <= ny < 8):
                    continue
                if graph[nx][ny] == '.':
                    q.append((nx,ny,cnt+1))
        graph = moveGraph(graph)
    return 0


print(bfs(graph))
