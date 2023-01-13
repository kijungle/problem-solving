#230113 1801~1822
#1806_G4 Prefix Sum
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
preSum = [0]*n
start = end = 0
ans = 1e9

preSum[0] = arr[0]
for i in range(1, n):
    preSum[i] = arr[i] + preSum[i-1]
preSum = [0] + preSum

while end <= n and start <= end:
    _sum = preSum[end] - preSum[start]
    #print(start, end, _sum)
    if _sum < s:
        end += 1
    else:
        ans = min(ans, end-start)
        start += 1
   
print(0 if ans == 1e9 else ans)
sys.exit()