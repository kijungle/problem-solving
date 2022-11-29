#221129 1939~1959
#11729_S1 Recursion
import sys
input = sys.stdin.readline

n = int(input())
def hanoi(n,a,b,c):
    if n == 1:
        print(a,c)
    else:
        hanoi(n-1,a,c,b)
        print(a,c)
        hanoi(n-1,b,a,c)

print(2**n-1)
hanoi(n,1,2,3)