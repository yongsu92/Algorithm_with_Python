import sys
sys.stdin = open('input_move.txt','r')

n = int(input())
moves = input().split()
dx = [0,0,1,-1]
dy = [1,-1,0,0]
x = y = 0
move = {'R':0,'L':1,'D':2,'U':3}

for go in moves:
    tx,ty = x+ dx[move[go]],y+dy[move[go]]
    if tx <0 or ty< 0 or tx >= n or ty >= n: continue
    x,y = tx,ty

print(x+1,y+1)