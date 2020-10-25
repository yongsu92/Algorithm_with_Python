def recursion_function(i):
    if i == 10:
        return
    print(f'{i} 번째 함수에서 {i+1} 번쨰 재귀함수를 호출합니다.')
    recursion_function(i+1)
    print(f'{i} 번째 재귀함수가 끝났습니다.')

# recursion_function(1)

def factorial(i):
    if i < 1:
        return 1
    return i * factorial(i-1)

print(factorial(5))

def factorial_loop(i):
    result = 1

    for num in range(1,i+1):
        result *= num
    return result

print(factorial_loop(5))