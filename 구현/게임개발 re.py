import sys
sys.stdin = open('input_game.txt','r')

n,m = map(int,input().split())
x,y,d = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(n)]
check = [[False]*m for _ in range(n)]
check[x][y] = True
dx = [-1,0,1,0]
dy = [0,1,0,-1]
count =1
while True:
    # 방향 회전
    for i in range(4):
        d -= 1
        if d == -4:
            d = 0
        tx,ty = x+dx[d],y+dy[d]
        if tx <0 or ty <0 or tx >= n or ty >=m: continue
        if check[tx][ty] or G[tx][ty]: continue
        check[tx][ty] = True
        x,y = tx,ty
        count += 1
        break
    else:
        # 뒤로 한칸이동
        x = x+(dx[d]*(-1))
        y = y+(dy[d]*(-1))
        if G[x][y]:
            break
print(count)