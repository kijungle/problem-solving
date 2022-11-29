#221129 1438~1524
#1891_G4 Recursion
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
d, num = map(str, input().split())
d = int(d)
x,y = map(int, input().split())


def fourArea(x,y,size,idx):
    if idx == d:
        return [x, y]
    pos = int(num[idx])
    size //= 2
    if pos == 1:
        return fourArea(x,y+size,size,idx+1)
    elif pos == 2:
        return fourArea(x,y,size,idx+1)
    elif pos == 3:
        return fourArea(x+size,y,size,idx+1)
    elif pos == 4:
        return fourArea(x+size,y+size,size,idx+1)

def findfourArea(x,y,size,str,depth):
    #print(x,y,size)
    if depth == d:
        print(str)
        sys.exit()
    size = size // 2
    if x <= pos[0] < x+size:
        if y <= pos[1] < y+size:
            findfourArea(x,y,size,str+'2',depth+1)
        elif y+size <= pos[1] < y+2*size:
            findfourArea(x,y+size,size,str+'1',depth+1)
        else:
            print(-1)
            sys.exit()
    elif x+size <= pos[0] < x+2*size:
        if y <= pos[1] < y+size:
            findfourArea(x+size,y,size,str+'3',depth+1)
        elif y+size <= pos[1] < y+2*size:
            findfourArea(x+size,y+size,size,str+'4',depth+1)
        else:
            print(-1)
            sys.exit()
    else:
        print(-1)
        sys.exit()
pos = fourArea(0,0,2**d,0)
#print(pos)
pos[0] -= y
pos[1] += x
#print(pos)
findfourArea(0,0,2**d,'',0)
# d = 3 2**3