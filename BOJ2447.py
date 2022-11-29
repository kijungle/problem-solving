#221129 1716~1731
#2447_G5 Divede and Conquer
import sys
input = sys.stdin.readline
n = int(input())
asterisk = [[' ' for _ in range(n)] for _ in range(n)]


def printAsterisk(x,y,size):
    if size == 3:
        asterisk[x][y] = '*'
        asterisk[x][y+1] = '*'
        asterisk[x][y+2] = '*'
        asterisk[x+1][y] = '*'    
        asterisk[x+1][y+2] = '*'
        asterisk[x+2][y] = '*'
        asterisk[x+2][y+1] = '*'
        asterisk[x+2][y+2] = '*'
        return

    else:
        size = size // 3
        printAsterisk(x,y,size)
        printAsterisk(x,y+size,size)
        printAsterisk(x,y+2*size,size)

        printAsterisk(x+size,y,size)
        printAsterisk(x+size,y+2*size,size)

        printAsterisk(x+2*size,y,size)
        printAsterisk(x+2*size,y+size,size)
        printAsterisk(x+2*size,y+2*size,size)


printAsterisk(0,0,n)
for i in range(n):
    for j in range(n):
        print(asterisk[i][j],end='')
    print()