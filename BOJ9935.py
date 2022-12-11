#221211 1458~1524
#9935_G4 Stack

import sys
input = sys.stdin.readline

#len(string) <= 1,000,000 , len(bomb) <= 36
string = input().rstrip()
bomb = input().rstrip()
end = bomb[-1]
stack = []
def deleteBomb(stack):
    for i in range(len(bomb)):
        stack.pop()

def checkBomb(stack):
    check = stack[-(len(bomb)):]
    for i in range(len(check)):
        if bomb[i] != check[i]:
            return False
    return True

for i in range(len(string)):
    stack.append(string[i])
    if len(stack) >= len(bomb) and string[i] == end:
        if checkBomb(stack):
            deleteBomb(stack)

if stack:
    for i in stack:
        print(i, end='')
else:
    print('FRULA')
# mirkovC4nizCC44
# C4
# m i r k o v n i z 