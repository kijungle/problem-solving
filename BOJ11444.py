#221201 1619~1645
#11444_G2 Matrix Fibonacci
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
p = 1000000007
if n == 0:
    print('0')
    sys.exit()
if n == 1 or n == 2:
    print('1')
    sys.exit()

# Multiply of Matrix in fibo O(lgn)
# f(n+1)  =  1f(n) + 1f(n-1) = 1 1 ^ n   f(n)
# f(n)    =  1f(n) + 0f(n-1) = 1 0   f(n-1)

def mulMat(a,b):
    global p
    ret = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ret[i][j] += a[i][k] * b[k][j]
            ret[i][j] %= p
    return ret

def fibo(n, m):
    if n == 1:
        return m
    if n % 2 == 0:
        tmp = fibo(n//2, m)
        return mulMat(tmp, tmp)
    else:
        tmp = fibo(n//2, m)
        return mulMat(tmp,(mulMat(tmp,m)))

matrix = [[1,1],[1,0]]
print(fibo(n-1,matrix)[0][0])
# 1 1   1   1
# 1 0   0   1