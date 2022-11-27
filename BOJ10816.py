#221127 2103~2116
#10816_S4 Binary Search
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
keys = list(map(int, input().split()))
count = [0] * m
countDict = dict()
arr.sort()

for num in arr:
    countDict[num] = 0
for num in arr:
    countDict[num] += 1

def bSearch(key, s, e):
    if s > e:
        return 0
    m = (s+e) // 2
    if key == arr[m]:
        return countDict[key]
    elif key < arr[m]:
        return bSearch(key, s, m-1)
    elif key > arr[m]:
        return bSearch(key, m+1, e)

for i in range(len(keys)):
    count[i] = bSearch(keys[i], 0, n-1)
print(*count)