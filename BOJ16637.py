#221208 1740~1913
#16637_G3 Brute Force

import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
string = list(input().rstrip())
op = []
num = []
ans = -1e9
for ch in string:
    if ch == '+' or ch == '-' or ch == '*':
        op.append(ch)
    else:
        num.append(int(ch))

def calc(form, num2, op):
    num1 = form.pop()
    if op == '+':
        form.append(num1+num2)
    elif op == '-':
        form.append(num1-num2)
    elif op == '*':
        form.append(num1*num2)
def calculate(form):
    if len(form) == 1:
        return form[0]
    else:
        num1 = form.pop(0)
        while form:
            op = form.pop(0)
            num2 = form.pop(0)
            if op == '+':
                num1 = num1 + num2
            elif op == '-':
                num1 = num1 - num2
            elif op == '*':
                num1= num1 * num2
    return num1

def dfs(form, idx, bracket):
    global ans
    if idx == len(op):
        ans = max(ans, calculate(deepcopy(form)))
        return
    if bracket:
        form.append(op[idx])
        form.append(num[idx+1])
        dfs(form, idx+1, False)
        form.pop()
        form.pop()
    else:
        form.append(op[idx])
        form.append(num[idx+1])
        dfs(form, idx+1, False)
        form.pop()
        form.pop()
        calc(form, num[idx+1], op[idx])
        dfs(form, idx+1, True)

dfs([num[0]],0,False)
print(ans)
# 8 * 3 + 5
# [8] -> [24], [8*3]
# [24] -> [24+5]
# [8*3] -> [8*8], [8*3+5]