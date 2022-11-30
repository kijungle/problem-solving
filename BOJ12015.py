#221130 1622~1652
#12015_G2 LIS (Binary Search)
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = []
ans.append(arr[0])

def binarySearch(key, s, e):
    while s < e:
        mid = (s+e)//2
        if ans[mid] < key:
            s = mid + 1
        else:
            e = mid

    return e
    
for i in range(1, n):
    if ans[-1] < arr[i]:
        ans.append(arr[i])
    else:
        idx = binarySearch(arr[i], 0, len(ans)-1)
        ans[idx] = arr[i]

print(len(ans))
    

# 7 8 1 2 3 4 5 6
# 1 8 
# 1 2 
# 7 8  
# 0  10 10 