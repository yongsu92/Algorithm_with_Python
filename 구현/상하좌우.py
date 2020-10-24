'''
10
R R R U D D L L D U
'''

# 시간 복잡도 이동 횟수 O(N)

import sys

N = int(sys.stdin.readline())
directions = list(sys.stdin.readline().split())
x = y = 1
moves = {'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)}

for dir in directions:
    dx,dy = moves[dir]
    tx,ty = x+dx,y+dy
    if tx <1 or ty <1 or tx == N or ty == N:
        continue
    x,y = tx,ty

print(tx,ty)