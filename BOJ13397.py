##221204 1505~1615
#13397_G4 parametric search
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0


def isValid(num):
    global m
    low = arr[0]
    high = arr[0]
    d = 1
    for i in range(len(arr)):
        if high < arr[i]:
            high = arr[i]
        if low > arr[i]:
            low = arr[i]
        if high - low > num:
            d += 1
            low = arr[i]
            high = arr[i]
    if d > m:
        return True
    else:
        return False

def bSearch(s,e): 
    global ans
    #print(s,e)
    if s > e:
        return s
    mid = (s+e) // 2
    if isValid(mid):
        s = mid+1
        return bSearch(s,e)
    else:
        e = mid-1
        return bSearch(s,e)

print(bSearch(0, max(arr)))
