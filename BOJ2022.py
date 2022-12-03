#221203 2012~2021
#2022_G5 Math

import sys
input = sys.stdin.readline

x,y,c = map(float, input().split())
w = 0
s,e = 0, min(x,y)

def calculate(x,y,w):
    h1 = (x**2-w**2)**0.5
    h2 = (y**2-w**2)**0.5
    c = h1*h2 / (h1+h2)
    return c

while e-s > 0.000001:
    m = (s+e)/2
    if calculate(x,y,m) >= c:
        w = m
        s = m
    else:
        e = m
print(w)
# 30 40 10
# w = w1 + w2 =  c*w / h2 + c*w / h1 = cw(h1+h2) /h1h2
# c = h1h2/h1+h2
#  h1 = sqrt(x**2-w**2), h2 = sqrt(y**2-w**2)
# 