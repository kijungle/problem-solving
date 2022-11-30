#221130 2132~
#10830_G4 Divide and Conquer
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
p = 1000
cnt = 0

def multiply(a,b):
    global cnt
    cnt += 1
    global p
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += (a[i][k] * b[k][j])
            res[i][j] %= p

    return res

def power(b):
    global p
    if b == 1:
        return matrix
    tmp = power(b//2)
    if b % 2 == 0:
        return multiply(tmp, tmp)
    else:
        return multiply(multiply(matrix, tmp), tmp)
# 5 -> 2/2/1 -> 1/1/1/1/1
res = power(b)
for i in range(n):
    for j in range(n):
        print(res[i][j]%p, end=' ')
    print('')
