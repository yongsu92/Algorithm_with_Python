'''
5 6
101010
111111
000001
111111
111111
'''
import sys
import collections
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y):
    Q = collections.deque([(x,y)])
    visit[x][y] = 1
    while Q:
        x,y = Q.popleft()
        for i in range(4):
            tx,ty = x+dx[i],y+dy[i]
            if tx <0 or ty <0 or tx == N or ty == M: continue
            if not G[tx][ty] or visit[tx][ty]: continue
            Q.append((tx,ty))
            visit[tx][ty] = visit[x][y] + 1
    return visit[N-1][M-1]

N,M = map(int,input().split())
G = [list(map(int,sys.stdin.readline().rstrip('\n'))) for _ in range(N)]
visit = [[0]*M for _ in range(N)]

result = bfs(0,0)
print(result)