#221126 2257~0028
#4574_G1 DFS+BruteForce
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
t = 1
dx = [1,-1,0,0]
dy = [0,0,1,-1]
flag = False
def canPlaceTile(x,y,num):
    gx = x // 3 * 3
    gy = y // 3 * 3
    for i in range(9):
        if graph[x][i] == num:
            return False
    for i in range(9):
        if graph[i][y] == num:
            return False
    for i in range(3):
        for j in range(3):
            if graph[gx+i][gy+j] == num:
                return False
    return True

def dfs(cnt, t):
    global flag
    if cnt == 81:
        # 이상하게도 이 부분이 2번 이상 방문함.
        if flag:
            return
        flag = True
        print('Puzzle', t)
        for i in range(9):
            for j in range(9):
                print(graph[i][j], end ='')
            print()
        return True

    x = cnt // 9
    y = cnt % 9
    if graph[x][y] == 0:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not (0 <= nx < 9 and 0 <= ny < 9):
                continue
            if graph[nx][ny] != 0:
                continue

            for i in range(9):
                for j in range(9):
                    if i == j or tileList[i][j] == False:
                        continue
                    if canPlaceTile(x,y,i+1) and canPlaceTile(nx,ny,j+1):
                        #print('put', x, y, nx, ny, i+1, j+1)
                        graph[x][y] = i+1
                        graph[nx][ny] = j+1
                        tileList[i][j] = False
                        tileList[j][i] = False
                        if (dfs(cnt+1,t)):
                            return True
                        tileList[i][j] = True
                        tileList[j][i] = True
                        graph[x][y] = 0
                        graph[nx][ny] = 0
    else:
        dfs(cnt+1,t)
    return False

while(True):
    n = int(input())
    if n == 0:
        sys.exit()
    tileList = [[True] * 9 for _ in range(9)]
    usedTile = []
    graph = [[0] * 9 for _ in range(9)]
    for _ in range(n):
        inputList = list(input().rstrip().split())
        numList = [int(inputList[0]), int(inputList[2])]
        x1 = ord(inputList[1][0]) - ord('A')
        y1 = int(inputList[1][1])-1
        x2 = ord(inputList[3][0]) - ord('A')
        y2 = int(inputList[3][1])-1
        graph[x1][y1] = numList[0]
        graph[x2][y2] = numList[1]
        usedTile.append((sorted(numList)))
    inputList = list(input().rstrip().split())
    for i in range(0, 9):
        x = ord(inputList[i][0]) - ord('A')
        y = int(inputList[i][1]) - 1
        graph[x][y] = i+1
    for tile in usedTile:
        x,y = tile[0], tile[1]
        tileList[x-1][y-1] = False
        tileList[y-1][x-1] = False
    
    #for i in range(9):
    #    print(*tileList[i])
    flag = False
    dfs(0,t)
    t += 1
    