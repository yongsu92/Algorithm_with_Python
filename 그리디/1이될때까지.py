'''
25 3
'''

import sys

N,K = map(int,sys.stdin.readline().split())
count = 0
while N !=1:
    N = N-1 if N%K else N//K
    count +=1

# result = N//K + N%K
print(count)
# print(result)