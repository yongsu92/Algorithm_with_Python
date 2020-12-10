import sys

sys.stdin = open('input_law_of_num.txt')

n,m,k = map(int,input().split())
arr = sorted(list(map(int,input().split())),reverse=True)
result = arr[0]*k * (m//k) + arr[1]*(m%k)*1
print(result)