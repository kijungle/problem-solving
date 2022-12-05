#221205 2333~2353
#10986_G3 Math + Prefix Sum, O(n+m)
n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefixSum = [0 for _ in range(n+1)]
modular = [[] for _ in range(m)]
modular[0].append(prefixSum[0])
ans = 0
# n < 10^6, m < 10^3
#O(n)
for i in range(1, n+1):
    prefixSum[i] = prefixSum[i-1] + arr[i-1]
    k = prefixSum[i] % m
    modular[k].append(prefixSum[i])
#O(m)
for i in range(m):
    k = len(modular[i])
    ans += k*(k-1) // 2
#O(n+m)
print(ans)
# 10^6
# % m = 0, 1, 2 .. m-1
# A = kA + R  B-A = k(A-B) 
# B = kB + R
# [(3,6,9,0), (1,7)]
# 30 60 90 36 39 69 17