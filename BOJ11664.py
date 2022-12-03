#221203 2320 ~ 2339
#11664_G5 Binary Search

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
x1,y1,z1,x2,y2,z2,a,b,c = map(float,input().split())
ans = 1e9

def dist(x1,y1,z1,x2,y2,z2):
    return ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2) ** 0.5

def bSearch(sx,sy,sz,ex,ey,ez):
    #print(sx,sy,sz,ex,ey,ez)
    global ans,a,b,c
    mx,my,mz = (sx+ex)/2, (sy+ey)/2, (sz+ez)/2
    sDist = dist(sx,sy,sz,a,b,c)
    eDist = dist(ex,ey,ez,a,b,c)
    mDist = dist(mx,my,mz,a,b,c)
    if abs(sDist-eDist) <= 1e-6:
        return mDist
    if sDist < eDist:
        ex, ey, ez = mx, my, mz
        return bSearch(sx,sy,sz,ex,ey,ez)
    else:
        sx, sy, sz = mx, my, mz
        return bSearch(sx,sy,sz,ex,ey,ez)

print(bSearch(x1,y1,z1,x2,y2,z2))