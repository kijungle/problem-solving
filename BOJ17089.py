#221207 1708~1728
#17089_S1 DFS

import sys
input = sys.stdin.readline
ans = 1e9
n, m = map(int, input().split())
friends = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

def dfs(s, f, depth):
    global ans
    if depth == 2:
        if s in friends[f[-1]]:
            #print(f)
            tmp = len(friends[f[0]]) + len(friends[f[1]]) + len(friends[f[2]]) - 6
            ans = min(ans, tmp)
        return

    for i in friends[f[-1]]:
        if not visited[i]:
            visited[i] = True
            f.append(i)
            dfs(s, f, depth+1)
            f.pop()
            visited[i] = False
    
#O(N) * O(N+M)
# dfs = O(N+M)
for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    visited[i] = True
    dfs(i, [i], 0)

print(ans if ans != 1e9 else -1)