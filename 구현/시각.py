'''
5
'''

import sys

N = int(sys.stdin.readline())

# 초,분
count = 0
for k in range(0,N+1):
    for j in range(60):
        for i in range(60):
            # if '3' in list(str(i)) or '3' in list(str(j)) or '3' in list(str(k)):
            if '3' in str(i)+str(j)+str(k):
                count += 1

#  시
print(count)
