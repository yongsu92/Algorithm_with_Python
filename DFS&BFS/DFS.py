def dfs(graph,v):
    visit[v] = True
    print(v,end=' ')
    for w in graph[v]:
        if not visit[w]:
            dfs(graph,w)

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

dfs(graph,1)