#221123 1545~1608
#1080 S1 Greedy
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
matrixA = [list(map(int, input().rstrip())) for _ in range(n)]
matrixB = [list(map(int, input().rstrip())) for _ in range(n)]
ans = 0
def reverse(x,y,matrix):
    for i in range(x, x+3):
        for j in range(y, y+3):
            matrix[i][j] = 1 - matrix[i][j]

def checkSameMatrix(a,b):
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False

    return True


for i in range(0, n-2):
    for j in range(0, m-2):
        if matrixA[i][j] != matrixB[i][j]:
            reverse(i,j,matrixA)
            ans += 1
            continue
        if checkSameMatrix(matrixA, matrixB):
            break



if n <= 2 or m <= 2:
    if checkSameMatrix(matrixA, matrixB):
        print('0')
    else:
        print('-1')
    sys.exit()
print(ans if checkSameMatrix(matrixA, matrixB) else '-1')

