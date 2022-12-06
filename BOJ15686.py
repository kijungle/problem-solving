#221206 1759~1828
#15686_G5 Brute Force
import sys
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chicken = []
home = []
ans = 1e9
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i,j))
        if graph[i][j] == 1:
            home.append((i,j))
deleteNum = len(chicken) - m


def distance(graph):
    ret = 0
    for x,y in home:
        dist = 1e9
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 2:
                    dist = min(dist, abs(i-x)+abs(j-y))
        ret += dist
    return ret

# O(13Cm * 2n) = O(1716 * 2 * n)
deleteCandidates = list(combinations(chicken, deleteNum))
for candidate in deleteCandidates:
    newGraph = deepcopy(graph)
    for x,y in candidate:
        newGraph[x][y] = 0
    ans = min(ans, distance(newGraph))
print(ans)