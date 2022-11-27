#221127 2119~2154
#1780_S2 Divde and Couquer
import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
paper = [0,0,0]
def checkPaper(x,y,n):
    color = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j] != color:
                nsize = n//3
                checkPaper(x,y,nsize)
                checkPaper(x,y+nsize,nsize)
                checkPaper(x,y+2*nsize,nsize)
                checkPaper(x+nsize,y,nsize)
                checkPaper(x+nsize,y+nsize,nsize)
                checkPaper(x+nsize,y+2*nsize,nsize)
                checkPaper(x+2*nsize,y,nsize)
                checkPaper(x+2*nsize,y+nsize,nsize)
                checkPaper(x+2*nsize,y+2*nsize,nsize)
                return
    
    paper[color] += 1

    



checkPaper(0,0,n)
print(paper[-1])#paper[2]
print(paper[0])
print(paper[1])