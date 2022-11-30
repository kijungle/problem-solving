#221130 2003~2013
#2630_S2 Divide and Conquer
import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
blue = white = 0


def dividePaper(x,y,size):
    global white, blue
    if size == 1:
        if graph[x][y] == 1:
            blue += 1
        else:
            white += 1
        return
    
    else:
        color = graph[x][y]
        flag = True
        for i in range(x, x+size):
            for j in range(y, y+size):
                if graph[i][j] != color:
                    flag = False
                    break
        if flag:
            if color == 0:
                white += 1
            else:
                blue += 1
        else:
            size //= 2
            dividePaper(x,y,size)
            dividePaper(x,y+size,size)
            dividePaper(x+size,y,size)
            dividePaper(x+size,y+size,size)
                


dividePaper(0,0,n)
print(white)
print(blue)