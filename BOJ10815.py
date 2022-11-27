#221127 2018~2031
#10815_S5 Binary Search
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
check = [0] * m
arr1.sort()

def bSearch(key, s, e):
    while s <= e:
        m = (s+e) // 2
        if arr1[m] == key:
            return True
        elif arr1[m] > key:
            e = m-1
        else:
            s = m+1
    return False
    

    
for i in range(len(arr2)):
    if bSearch(arr2[i],0,len(arr1)-1):
        check[i] = 1

print(*check)
#O(m lg n)