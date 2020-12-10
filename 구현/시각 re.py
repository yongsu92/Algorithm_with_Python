import sys
sys.stdin = open('input_time.txt','r')

N = int(input())
count = 0
for n in range(N+1):
    for i in range(60):
        for j in range(60):
            # if n == 3 or '3' in list(str(i)) or '3' in list(str(j)):
            if '3' in str(i)+str(n)+str(j):
                count +=1
print(count)