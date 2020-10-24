'''
a1
'''
import sys
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]
# dict_alpha = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
position= list(sys.stdin.readline())
y = int(ord(position[0])) - int(ord('a')) +1 # 아스키 코드값을 이용해서 문자열에 대한 숫자를 구할 수 있다.
# y = dict_alpha[position[0]]
x = int(position[1])
count = 0
for i in range(8):
    tx,ty = x+dx[i],y+dy[i]
    if tx <1 or ty <1 or tx > 8 or ty > 8: continue
    count +=1
print(count)