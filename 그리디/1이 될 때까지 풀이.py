import sys
sys.stdin = open('input_to_1.txt','r')


### 로그 시간 복잡도를 가지게 된다. ###

for t in range(1,int(input())+1):
    n,k = map(int,input().split())
    result = 0

    while True:

        target = (n//k)*k
        result += (n-target)
        n = target

        if n < k:
            break

        result += 1
        n //= k

    result += (n-1)
    print(result)