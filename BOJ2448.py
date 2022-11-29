#221129 1731~1745
#2448_G4 Divide and Conquer
import sys
input = sys.stdin.readline
n = int(input())
asterisk = [[' ' for _ in range(2*n)] for _ in range(n)]

def printAsterisk(x,y,size):
    if size == 3:
        asterisk[x][y] = '*'
        
        asterisk[x+1][y-1] = '*'
        asterisk[x+1][y+1] = '*'

        asterisk[x+2][y-2] = '*'
        asterisk[x+2][y-1] = '*'
        asterisk[x+2][y] = '*'
        asterisk[x+2][y+1] = '*'
        asterisk[x+2][y+2] = '*'
        return
    else:
        size //= 2
        printAsterisk(x,y,size)
        printAsterisk(x+size,y-size,size)
        printAsterisk(x+size,y+size,size)

printAsterisk(0,n-1,n)
for i in range(n):
    for j in range(2*n):
        print(asterisk[i][j], end='')
    print()