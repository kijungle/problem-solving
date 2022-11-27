#221127 1724~1759
#14391_S5 Bitmasking
import sys
input = sys.stdin.readline
n = int(input())
bitArray = [False for _ in range(21)]
for _ in range(n):
    cmd = input().rstrip().split()
    if cmd[0] == 'add':
        bitArray[int(cmd[1])] = True
    elif cmd[0] == 'remove':
        bitArray[int(cmd[1])] = False
    elif cmd[0] == 'check':
        print('1' if bitArray[int(cmd[1])] else '0')
    elif cmd[0] == 'toggle':
        bitArray[int(cmd[1])] = not bitArray[int(cmd[1])]
    elif cmd[0] == 'all':
        bitArray = [True for _ in range(21)]
    elif cmd[0] == 'empty':
        bitArray = [False for _ in range(21)]