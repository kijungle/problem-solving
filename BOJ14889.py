#221127 1811~1825
#14489_S2 BitMasking
import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
bit = (1<<n)
ans = sys.maxsize

def getStat(players):
    _sum = 0
    for i in players:
        for j in players:
            _sum += graph[i][j]
    return _sum
for i in range(1, bit):
    start = []
    link = []
    for j in range(n):
        if (i & (1<<j)):
            start.append(j)
        else:
            link.append(j)
    if len(start) == len(link):
       # print(start, link)
        ans = min(ans, abs(getStat(start) - getStat(link)))

print(ans)