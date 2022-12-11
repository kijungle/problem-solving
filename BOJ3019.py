#221211 2013 ~ 2035
#3019_S1 BruteForce IMPL
import sys
from copy import deepcopy
input = sys.stdin.readline


# 7개블록 모드 4 28개 블록떨어뜨리기 !
# 4개블록 떨구기 * C * check
# O(400check)
c, p = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

def solve(p):
    global ans
    if p == 1:
        for i in range(c):
            ans += 1
        for i in range(c-3):
            if arr[i] == arr[i+1] == arr[i+2] == arr[i+3]:
                ans += 1 
    elif p == 2:
        for i in range(c-1):
            if arr[i] == arr[i+1]:
                ans += 1
    elif p == 3:
        for i in range(c-2):
            if arr[i] == arr[i+1] and arr[i+1] + 1 == arr[i+2]:
                ans += 1
        for i in range(c-1):
            if arr[i] == arr[i+1] + 1:
                ans += 1
    elif p == 4:
        for i in range(c-2):
            if arr[i] == arr[i+1] + 1 and arr[i+1] == arr[i+2]:
                ans += 1
        for i in range(c-1):
            if arr[i] + 1 == arr[i+1]:
                ans += 1
    elif p == 5:
        for i in range(c-2):
            if arr[i] == arr[i+1] == arr[i+2]:
                ans += 1
            elif arr[i] == arr[i+2] and arr[i+1]+1 == arr[i]:
                ans += 1
        for i in range(c-1):
            if arr[i] == arr[i+1] + 1:
                ans += 1
            elif arr[i] + 1 == arr[i+1]:
                ans += 1
    # xxo o  ooo oo
    # ooo o .oxx xo
    # .   oo     xo
    elif p == 6:
        for i in range(c-2):
            if arr[i] == arr[i+1] == arr[i+2]:
                ans += 1
            elif arr[i] + 1 == arr[i+1] == arr[i+2]:
                ans += 1
        for i in range(c-1):
            if arr[i] == arr[i+1] + 2:
                ans += 1
            elif arr[i] == arr[i+1]:
                ans += 1
    # oxx ooo
    # ooo xxo
    elif p == 7:
        for i in range(c-2):
            if arr[i] == arr[i+1] == arr[i+2]:
                ans += 1
            elif arr[i] == arr[i+1] == arr[i+2] + 1:
                ans += 1
        for i in range(c-1):
            if arr[i] + 2== arr[i+1]:
                ans += 1
            elif arr[i] == arr[i+1]:
                ans += 1
    return ans
            
print(solve(p))