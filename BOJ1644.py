#230113 1823~1838
#1644_G3
import sys
input = sys.stdin.readline

n = int(input())
isPrime = [True] * (n+1)
primeNum = []
ans = 0
#Num of Prime : 283146
for i in range(2, n+1):
    if isPrime[i]:
        for j in range(i, n):
            if i * j <= n:
                isPrime[i*j] = False
            else:
                break

for i in range(2, n+1):
    if isPrime[i]:
        primeNum.append(i)

cnt = isPrime[2:].count(True)
s = e = 0
preSum = [0]*cnt

for i in range(cnt):
    try:
        preSum[i] = preSum[i-1] + primeNum[i]
    except IndexError:
        preSum[i] = 0
preSum = [0] + preSum

while e <= cnt:
    _sum = preSum[e] - preSum[s]
    if _sum < n:
        e += 1
    elif _sum > n:
        s += 1
    elif _sum == n:
        ans += 1
        s += 1
        e += 1

print(ans)