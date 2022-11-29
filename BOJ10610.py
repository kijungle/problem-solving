#221129 1546~1550
#10610_S4 ?
import sys
input = sys.stdin.readline
num = list(map(int,input().rstrip()))
if 0 not in num:
    print('-1')
    sys.exit()
if sum(num) % 3 != 0:
    print('-1')
    sys.exit()
num.sort(reverse=True)
for i in range(len(num)):
    print(num[i], end='')

