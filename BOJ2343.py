# 221204 0200~0216
#2343_S1 Binary Search

import sys
n,m = map(int,input().split())
arr = list(map(int, input().split()))
# 1 2 3 4 5 6 7 8 9 -> m개로 쪼개기
# sum(arr) / 3 = 15
# 1 ~ 45 로 탐색? -> 
s = max(arr)
e = sum(arr)
# mid = 23 -> 21/15/9 = 3 (1,45) -> (1,22)
# mid = 12 -> 10/11/7/8/9 = 5 -> (13,23)
# mid = 18 -> 15/13/17 -> (13,17)
# mid = 15 -> 15/13/8/9 -> (16,17)
# mid = 16 -> 3 -> (18,17)

def record(num):
    ret = 0
    total = 0
    for i in range(len(arr)):
        if total + arr[i] > num:
            total = arr[i]
            ret += 1
        else:
            total += arr[i]

    return ret
def bSearch(s,e):
    global m
    #print(s,e)
    if s > e:
        return s
    mid = (s+e)//2
    r = record(mid)
    #print(r,mid,s,e)
    #print('r',r, mid)
    if r < m:
        return bSearch(s, mid-1)
    else:
        return bSearch(mid+1, e)

print(bSearch(s,e))