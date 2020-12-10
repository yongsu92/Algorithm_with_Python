dx = [-2,-1,1,2,2,1,-1,-2]
dy = [-1,-2,-2,-1,1,2,2,1]

n = list('c2')
x = ord(n[0])-97
y = int(n[1])-1
count = 0
for i in range(8):
    tx,ty = x+dx[i],y+dy[i]
    if tx <0 or ty <0 or tx >=8 or ty >= 8: continue
    count += 1
print(count)
