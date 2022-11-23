#221123 1753~1806
#1182 S2 Bruteforce & BackTracking
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n, s = map(int, input().split())
permutation = list(map(int, input().split()))
ans = 0
def backTracking(idx, _sum):
    global ans, s
    if idx >= n:
        return
    _sum += permutation[idx]
    if _sum == s:
        ans += 1
        
    backTracking(idx+1, _sum)
    backTracking(idx+1, _sum-permutation[idx])

backTracking(0,0)
print(ans)