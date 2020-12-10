import sys
sys.stdin = open('input_adventure.txt','r')

N = int(input())
rates = list(map(int,input().split()))
rates.sort()
rate = rates[0]
result = i = 0
count = 1
while True:
    if rate <= count:
        result += 1
        count = 0
    count += 1
    i += 1
    if i >= N:
        break
    rate = rates[i]
print(result)