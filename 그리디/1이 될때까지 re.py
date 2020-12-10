import sys

sys.stdin = open('input_to_1.txt','r')

for t in range(1,int(input())+1):
    N,K = map(int,input().split())
    count = 0
    while N != 1:
        # k 로 나누어 질 수 있느지
        if not N%K:
            N //=K
        # 나누어 떨어지지 않는다면 1을 뺀다.
        else:
            N -= 1

        count += 1

    print(count)

