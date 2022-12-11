#221211 2122~2132
#17070_G5 DFS
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
#가, 세, 대

ans = 0
def check(x,y,dir):
    if not (0 <= x < n and 0 <= y < n):
        return False
    if graph[x][y] == 1:
        return False
    if dir == 2:
        if graph[x-1][y] == 0 and graph[x][y-1] == 0:
            return True
        else:
            return False
    return True
def dfs(x,y,dir):
    global ans
    if x == n-1 and y == n-1:
        ans += 1
    if dir == 0:
        #가로
        nx, ny = x, y+1
        if check(nx,ny,0):
            dfs(nx,ny,0)
        #대각
        nx, ny = x+1, y+1
        if check(nx,ny,2):
            dfs(nx,ny,2)
    elif dir == 1:
        #세로
        nx, ny = x+1, y
        if check(nx,ny,1):
            dfs(nx,ny,1)
        #대각
        nx, ny = x+1, y+1
        if check(nx,ny,2):
            dfs(nx,ny,2)
    elif dir == 2:
        #가로
        nx, ny = x, y+1
        if check(nx,ny,0):
            dfs(nx,ny,0)
        #세로
        nx, ny = x+1, y
        if check(nx,ny,1):
            dfs(nx,ny,1)
        #대각
        nx, ny = x+1 ,y+1
        if check(nx,ny,2):
            dfs(nx,ny,2)

dfs(0,1,0)
print(ans)