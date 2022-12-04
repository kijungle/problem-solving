#221205 0108~0133
#16936_G5 DFS
import sys
from copy import deepcopy
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
visited = [False for _ in range(n)]
def dfs(idx,ans):
    if len(ans) == n:
        print(*ans)
        sys.exit()
    else:
        visited[idx] = True
        cur = arr[idx]
        if cur % 3 == 0:
            ncur = cur // 3
            for i in range(len(arr)):
                if arr[i] == ncur and not visited[i]:
                    visited[i] = True
                    ans.append(ncur)
                    dfs(i, ans)
                    ans.pop()
                    visited[i] = False
        ncur = cur * 2
        for i in range(len(arr)):
            if arr[i] == ncur and not visited[i]:
                visited[i] = True
                ans.append(ncur)
                dfs(i, ans)
                ans.pop()
                visited[i] = False


#O(n3)
for i in range(len(arr)):
    ans = [arr[i]]
    visited = [False for _ in range(n)]
    dfs(i,ans)
