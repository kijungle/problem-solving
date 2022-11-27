#221127 2117~2118
#11728_S5 ??
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(*sorted(arr1+arr2))