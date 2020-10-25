import sys
import collections
import time
sys.stdin = open('input_freezingice.txt','r')


dx = [0,-1,0,1]
dy = [-1,0,1,0]

def bfs(x,y):
    Q = collections.deque([(x,y)])
    check[x][y] = 1
    while Q:
        x,y = Q.popleft()
        for i in range(4):
            tx,ty = x+dx[i],y+dy[i]
            if tx < 0 or ty < 0 or tx == N or ty == M: continue
            if G[tx][ty] == 1 or check[tx][ty]: continue
            Q.append((tx,ty))
            check[tx][ty] = 1


def dfs(x,y):
    check[x][y] = 1
    for i in range(4):
        tx,ty = x+dx[i],y+dy[i]
        if tx < 0 or ty < 0 or tx == N or ty == M: continue
        if G[tx][ty] == 1 or check[tx][ty]: continue
        dfs(tx,ty)


N,M = map(int,sys.stdin.readline().split())
G = [list(map(int,list(sys.stdin.readline().rstrip('\n')))) for _ in range(N)]
check = [[0]*(M) for _ in range(N)]
count = 0

start_time = time.time()
for i in range(N):
    for j in range(M):
        if not G[i][j] and not check[i][j]:
            count += 1
            bfs(i,j)
end_time = time.time()
print(f'BFS time : {end_time-start_time} s')

count = 0
check = [[0]*(M) for _ in range(N)]
start_time = time.time()
for i in range(N):
    for j in range(M):
        if not G[i][j] and not check[i][j]:
            count += 1
            dfs(i,j)
end_time = time.time()
print(f'DFS time : {end_time-start_time} s')


print(count)