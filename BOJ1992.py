#221129 2024~2034
#1992_S1 Divide and Conquer
import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int,input().rstrip())) for _ in range(n)]

def quadTree(x,y,size):
    if size == 1:
        print(graph[x][y], end='')

    
    else:
        flag = True
        color = graph[x][y]
        for i in range(x, x+size):
            for j in range(y, y+size):
                if color != graph[i][j]:
                    flag = False
        if flag:
            print(color,end='')
        else:
            size //= 2
            print('(',end='')
            quadTree(x,y,size)
            quadTree(x,y+size,size)
            quadTree(x+size,y,size)
            quadTree(x+size,y+size,size)
            print(')',end='')
    

quadTree(0,0,n)
# (0(0011)(0(0111)01)1)