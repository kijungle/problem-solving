#221128 1914~1945
#1541_S2 Greedy
import sys
input = sys.stdin.readline
string = input().rstrip().split('-')
total = 0

def calculate():
    for i in range(len(string)):
        total = 0
        form = string[i].split('+')
        if len(form) != 0:
            for num in form:
                total += int(num)
            string[i] = total
    
    ret = int(string[0])
    for i in range(1, len(string)):
        ret -= int(string[i])
    return ret
print(calculate())
        

# a + b - c
# a - b + c - d => a - (b+c) - d
