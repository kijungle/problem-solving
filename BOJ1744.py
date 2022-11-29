#221129 1422~1436
#1744_G4 Greedy
import sys
input = sys.stdin.readline
n = int(input())
neg = []
pos = []
zero = 0
ans = 0
for _ in range(n):
    num = int(input())
    if num > 0:
        pos.append(num)
    elif num < 0:
        neg.append(num)
    else:
        zero += 1
pos.sort()
neg.sort(key = lambda x : abs(x))
# positive number
while len(pos) > 1:
    num1 = pos.pop()
    num2 = pos.pop()
    if num1 == 1 or num2 == 1:
        ans += (num1+num2)
    else:
        ans += num1 * num2
if pos:
    ans += pos.pop()
# negative number
while len(neg) > 1:
    num1 = neg.pop()
    num2 = neg.pop()
    ans += (num1 * num2)
if neg:
    if zero == 0:
        ans += neg.pop()
        

print(ans)