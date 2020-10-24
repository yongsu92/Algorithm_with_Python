'''
3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4
'''
import sys

N,M = map(int,sys.stdin.readline().split())
max_number =0

for _ in range(N):
    line_min = min(list(map(int,sys.stdin.readline().split())))
    # if max_number < line_min:
    #     max_number = line_min
    max_number = max(max_number,line_min)

print(max_number)