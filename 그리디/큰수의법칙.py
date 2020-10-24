'''
5 8 3
2 4 5 4 6

5 7 2
3 4 3 4 3
'''
import sys

N,M,K = map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))
numbers.sort(reverse=True)
max_num = numbers[0]
second_num = numbers[1]
count = True
result = 0


# 1. 방법 1
# while M:
#     if max_num == second_num:
#         result += max_num*M
#         break
#     if count:
#         result += max_num*K
#         M -= K
#         count = False
#         continue
#     else:
#         result += second_num
#         M -=1
#         count = True
#         continue


# 2. 방법 2
#
# while True:
#     for i in range(K):
#         if M == 0:
#             break
#         result += max_num
#         M -= 1
#     if M == 0:
#         break
#     result += second_num
#     M -=1

# 3. 방법 3 - 반복 수열이라는 것을 인지

count = M//(K+1) + M%(K+1)
result += count*max_num + (M-count)*second_num
print(result)