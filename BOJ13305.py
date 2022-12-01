#221201 1546~1617
#13305_S3 Greedy
import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
ans = [0] * n # ans[n] = (n)th -> (n-1)th cheapest cost
minPrice = price[0]
ans[0] = dist[0]*price[0]

for i in range(1,n-1):
    if minPrice <= price[i]:
        ans[i] = dist[i] * minPrice
    else:
        minPrice = price[i]
        ans[i] = dist[i] * minPrice

print(sum(ans))