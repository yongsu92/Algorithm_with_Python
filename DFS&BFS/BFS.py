import collections


def bfs(graph,v,visit):
    visit[v] = True
    Q = collections.deque([v])
    while Q:
        v = Q.popleft()
        print(v,end = ' ')
        for w in graph[v]:
            if not visit[w]:
                Q.append(w)
                visit[w] = True




graph  =[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visit = [False]*9

bfs(graph,1,visit)