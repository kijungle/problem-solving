#221123 1814~1831
#1062 G4 BruteForce & BackTracking
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
words = []
for _ in range(n):
    word = set(list(input().rstrip()))
    words.append(word)
teached = [0] * 26
ans = 0
if k < 5:
    print('0')
    sys.exit()
teached[ord('a')-ord('a')] = 1
teached[ord('n')-ord('a')] = 1
teached[ord('t')-ord('a')] = 1
teached[ord('i')-ord('a')] = 1
teached[ord('c')-ord('a')] = 1

def canSpeak(word):
    for alpha in word:
        if teached[ord(alpha)-ord('a')] == 0:
            return False
    return True

def backTracking(n, alpha):
    global ans
    #print(teached)
    if alpha >= 26:
        return

    if n == k-5:
        cnt = 0
        for word in words:
            if canSpeak(word):
                cnt += 1
        ans = max(ans, cnt)
        return
    
    if teached[alpha] == 1:
        backTracking(n, alpha+1)
    else:
        teached[alpha] = 1
        backTracking(n+1, alpha)
        teached[alpha] = 0
        backTracking(n, alpha+1)
    

# n = Teached alphabet
# alpha = learn alphabet
backTracking(0,0)
print(ans)
    
    