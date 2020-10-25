def fibonacci(x):
    if x == 1 or x == 2:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)

print(fibonacci(10))

# Memoization
d = [0]*101

def fibo(x):

    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)

    return d[x]
print(fibo(100))

dd = [0]*101
def fibo_loop(x):
    # 재귀를 사용하게 되면,오버헤드가 발생할 수 있기 때문에 반복문으로 처리할 수 있다.
    for i in range(1,x+1):
        if i == 1 or i == 2:
            dd[i] = 1
            continue
        dd[i] = dd[i-1]+dd[i-2]

    return dd[x]
print(fibo_loop(100))