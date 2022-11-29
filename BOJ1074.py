#221129 1416~1421
#1074_S1 Divede and Conquer
import sys
input = sys.stdin.readline
n, r, c = map(int, input().split())
dx = [0,0,1,1]
dy = [0,1,0,1]
cnt = 0
# 2^(2*n) // 4 = 16


def zTraverse(x,y,size):
    global cnt
    if not (x<=r<x+size and y<=c<y+size):
        cnt += size*size
        return

    if size == 2:
        #print(x,y,size)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            cnt += 1
            if nx == r and ny == c:
                print(cnt-1)
                sys.exit()

    
    
    size = size // 2
    zTraverse(x,y,size)
    zTraverse(x,y+size,size)
    zTraverse(x+size,y,size)
    zTraverse(x+size,y+size,size)
    

# size = 2**3 = 8
# 4
# 2 2 2 2

zTraverse(0,0,2**n)