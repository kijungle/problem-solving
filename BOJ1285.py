#221130 1653~1729
#1285_G1 bitmasking + greedy
import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
revGraph = [i[:] for i in graph]
ans = 401
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'H':
            graph[i][j] = 0
            revGraph[i][j] = 1
        else:
            graph[i][j] = 1
            revGraph[i][j] = 0

for b in range(1 << n):
    # 000 001 010 011 100 101 110 111
    tmpGraph = []
    #Flip Row as bit
    for i in range(n):
        if b & (1 << i):
            tmpGraph.append(revGraph[i][:])
        else:
            tmpGraph.append(graph[i][:])
    
    #Flip Column in greedy
    _sum = 0
    for j in range(n):
        original = 0
        #min(original sum, reverse sum)
        #reverse sum = n - original sum
        for i in range(n):
            original += tmpGraph[i][j]
        _sum += min(original, n-original)
    
    ans = min(ans, _sum)

print(ans)