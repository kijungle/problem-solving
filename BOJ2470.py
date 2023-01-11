#230111 1635~1657
#2470_G5 Two Pointer
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
s, e = 0, n-1
ans = 1e11
ansVal = [arr[s],arr[e]]
while s < e:
    tmp = arr[s] + arr[e]
    if ans > abs(tmp):
        ans = abs(tmp)
        ansVal = [arr[s], arr[e]]
    if tmp < 0:
        s += 1
    else:
        e -= 1

print(*ansVal)
