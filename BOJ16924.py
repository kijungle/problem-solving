#221205 0028~0106
#16924_S2 BruteForce

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
depth = (min(n,m)-1) // 2
empty = [['.'] * m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def isEmpty(g1):
    for i in range(n):
        for j in range(m):
            if g1[i][j] != '.':
                return False

    return True
        
def deleteCross(x,y,size):
    #print('Deleting', x, y, size)
    graph[x][y] = '.'

    for i in range(1, size+1):
        graph[x-i][y] = '.'
        graph[x+i][y] = '.'
        graph[x][y+i] = '.'
        graph[x][y-i] = '.'

def checkCross(x,y,size):
    #print('Checking', x+1, y+1, size)
    for i in range(4):
        for s in range(1, size+1):
            nx = x + dx[i] * s
            ny = y + dy[i] * s
            if graph[nx][ny] != '*':
                return False

    return True
    
def solve():
    ans = []
    # n * m * m = 10
    for size in range(1, depth+1):
        for i in range(size,n-size):
            for j in range(size,m-size):
                if graph[i][j] == '.':
                    continue
                if checkCross(i,j,size):
                    ans.append([i+1,j+1,size])
    
    for x,y,size in ans:
        deleteCross(x-1,y-1,size)
        if isEmpty(graph):
            return ans
    return -1   


            
ans = solve()
if ans == -1:
    print(ans)
else:
    print(len(ans))
    for i in ans:
        print(*i)