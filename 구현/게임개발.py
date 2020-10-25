'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 0 0 1
1 1 1 1
'''
import sys

def turn():
    global d
    d -= 1
    if d == -1:
        d = 3
N,M = map(int,sys.stdin.readline().split())
x,y,d = map(int,sys.stdin.readline().split())
G = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
check = [[0]*(M) for _ in range(N)]
check[x][y] = 1

# 방향을 인덱스로 사용하는 아이디어가 필요하였다.
dx = [-1,0,1,0]
dy = [0,1,0,-1]

count = 1
turn_left = 0
while True:
    turn()
    tx,ty = x+dx[d],y+dy[d]
    if tx <0 or ty <0 or tx == N or ty == M or G[tx][ty] == 1 or check[tx][ty] ==1:
        turn_left +=1
        if turn_left == 4:
            tx, ty = x - dx[d], y - dy[d]
            if G[tx][ty] == 1:
                break
            x, y = tx, ty
            turn_left = 0
        continue
    x,y = tx,ty
    check[tx][ty] = 1
    count += 1
    turn_left = 0
print(count)