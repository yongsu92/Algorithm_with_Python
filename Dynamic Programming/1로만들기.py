N = 26
start = 1
d = [5,3,2,1]

def dfs(start):

    if start == N:
        print('여기있어')
        return



    for i in range(4):
        print(i)
        if d[i] != 1:
            start *= d[i]
            print(start,'in if')
        else:
            start -= d[i]

        if start > N:
            start //= d[i]
            return start
        print(start)
        dfs(start)
        print('재귀끝',start)

dfs(start)
