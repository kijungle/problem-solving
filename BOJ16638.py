#221210 1331~1428
#16638_G1 DFS+Stack

import sys
input = sys.stdin.readline

n = int(input())
string = input().rstrip()
num = []
op = []
ans = -1e9
order = {'(':0, '-':1, '+':1, '*':2}
for ch in string:
    if ch == '+' or ch == '-' or ch == '*':
        op.append(ch)
    else:
        num.append(ch)
#(3+8)*(7-9)*2
def calc(n1, n2, op):
    if op == '+':
        return n1+n2
    elif op == '-':
        return n1-n2
    elif op == '*':
        return n1*n2
def postfix(form):
    form = list(form)
    st = []
    ret = []
    for i in range(len(form)):
        if '0' <= form[i] <= '9':
            ret.append(int(form[i]))
        elif form[i] == '(':
            st.append(form[i])
        elif form[i] == ')':
            while st[-1] != '(':
                ret.append(st.pop())
            st.pop()
        else:
            while st and order[form[i]] <= order[st[-1]]:
                ret.append(st.pop())
            st.append(form[i])
    while st:
        ret.append(st.pop())
    return ret

def calculate(form):
    form = postfix(form)
    st = []
    for i in range(len(form)):
        if form[i] == '+':
            n1 = st.pop()
            n2 = st.pop()
            st.append(n2+n1)
        elif form[i] == '-':
            n1 = st.pop()
            n2 = st.pop()
            st.append(n2-n1)
        elif form[i] == '*':
            n1 = st.pop()
            n2 = st.pop()
            st.append(n2*n1)
        else:
            st.append(form[i])
    return st[-1]
# 3 + 8 * 7 - 9 * 2
def dfs(idx, form, bracket):
    global ans
    if idx == len(op):
        ans = max(ans, calculate(form))
        return
    if bracket:
        dfs(idx+1, form+op[idx]+num[idx+1], False)
    else:
        dfs(idx+1, form+op[idx]+num[idx+1], False)
        dfs(idx+1, form[:-1] + '(' + num[idx] + op[idx] + num[idx+1] + ')', True)


dfs(0, num[0], False)
print(ans)