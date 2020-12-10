import sys
sys.stdin = open('input_cards.txt','r')

for t in range(1,int(input())+1):
    n,m = map(int,input().split())
    result = 0
    for _ in range(n):
        min_val = 10001
        for i in list(map(int,input().split())):
            if min_val > i:
                min_val = i
        if result < min_val:
            result = min_val
    print(result)
