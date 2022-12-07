#221207 1729~1755
#17406_G4 BruteForce + Implementation
import sys
from copy import deepcopy
from itertools import permutations
input = sys.stdin.readline



def minValue(graph):
    ret = 1e9
    for i in range(n):
        tmp = 0
        for j in range(m):
            tmp += graph[i][j]
        ret = min(ret, tmp)
    return ret

# O(NM) * size (50)
def rotate(x,y,size,graph):
    if size == 0:
        return
    up = graph[x-size][y-size]
    right = graph[x-size][y+size]
    down = graph[x+size][y+size]
    left = graph[x+size][y-size]
    # 위 -> 오 size * 2 번 
    #print('UP', size)
    for col in range(y-size+1, y+size+1):
        #print(x-size, col)
        npos = graph[x-size][col]
        graph[x-size][col] = up
        up = npos
    # 오 -> 아
    #print('Right', size)
    for row in range(x-size+1, x+size+1):
        #print(row, y+size)
        npos = graph[row][y+size]
        graph[row][y+size] = right
        right = npos
    # 아 -> 왼
    #print('Down', size)
    for col in range(y+size-1, y-size-1, -1):
        #print(x+size, col)
        npos = graph[x+size][col]
        graph[x+size][col] = down
        down = npos
    # 왼 -> 위
    #print('Left', size)
    for row in range(x+size-1, x-size-1, -1):
        #print(row, y-size)
        npos = graph[row][y-size]
        graph[row][y-size] = left
        left= npos
    rotate(x,y,size-1,graph)


n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cmd = []
ans = 1e9
# k : 6! = 720 * 50 O(NM) 720 * 50 * 50 * 50 = 9e8 < 1e9
# k!O(N^2M)
for _ in range(k):
    r,c,s = map(int, input().split())
    x, y = r-1, c-1
    cmd.append((x,y,s))

order = list(permutations(cmd, k))
for commands in order:
    newGraph = deepcopy(graph)
    for x,y,s in commands:
        rotate(x,y,s,newGraph)
    ans = min(minValue(newGraph),ans)
print(ans)