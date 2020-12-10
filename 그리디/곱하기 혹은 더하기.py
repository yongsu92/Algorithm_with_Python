import sys
sys.stdin = open('input_plus_or_mul.txt')

for t in range(1,int(input())+1):
    n = list(map(int,list(input())))
    # arr = []
    #
    # for i in n:
    #     if not arr:
    #         arr.append(i)
    #         continue
    #     if arr[-1] <= 1:
    #         x = arr.pop()
    #         arr.append(x+i)
    #     else:
    #         x = arr.pop()
    #         arr.append(x*i)
    # print(arr[0])


    ######## 풀이 ##########

    result = n[0]
    for i in range(1,len(n)):
        x = n[i]
        if x <= 1 or result <=1:
            result += x
        else:
            result *= x
    print(result)