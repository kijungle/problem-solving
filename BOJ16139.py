#221205 2315~2329
#16139_S1 Prefix Sum
import sys
input = sys.stdin.readline

string = input().rstrip()
q = int(input())
frequency = [[0] * len(string) for _ in range(26)]
#frequency[n][k] = 글자 N 이 0~K 까지 나오는 빈도수
# n <= 200,000, q <= 200,000
#O(n) * 26
for i in range(26):
    ch = chr(i + ord('a'))
    fre = 0
    for j in range(len(string)):
        if string[j] == ch:
            fre += 1
        frequency[i][j] = fre

#O(q)
for _ in range(q):
    ch, l, r = map(str, input().split())
    l,r = int(l), int(r)
    if l == 0:
        print(frequency[ord(ch)-ord('a')][r])
    else:
        print(frequency[ord(ch)-ord('a')][r] - frequency[ord(ch)-ord('a')][l-1])