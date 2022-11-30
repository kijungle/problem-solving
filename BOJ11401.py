#221130 2049~2130
#11401_G1 Femat's Little Theorem
import sys
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int, input().split())
p = 1000000007

def rPower(a,b):
    if b == 1:
        return a%p
    elif b%2 == 1:
        return rPower((a*a)%p, b//2) * a % p
    else:
        return rPower((a*a)%p, b//2)
    
def rFact(n):
    ret = 1
    for i in range(2,n+1):
        ret = (ret * i) % p
    return ret

a = rFact(n)
b = (rFact(k) * rFact(n-k)) % p
b = rPower(b, p-2)
print((a*b)%p)
#nCk = n!/k!(n-k)! = (n!%p * (k!)^p-2 %p * (n-k)!^p-2 % p)%p
#Fermat's little Theorem (FIT)
# b^p-1 = 1 mod p -> b^-1 % p = b^-1 * b^p-1 = b^p-2
# a/b % p
# a * (b^-1 % p)
# a * (b^-1) * (b^p-1 % p)
# (a * b^p-2) % p
# (a%p) * (b^p-2 % p) % p