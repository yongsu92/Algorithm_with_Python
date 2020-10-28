N = int(input())
arr = [0]*(int(1e6)+1)
for i in range(2,N+1):
    arr[i] = arr[i-1]+1
    if not i%2:
        arr[i] = min(arr[i],arr[i//2]+1)
    if not i%3:
        arr[i] = min(arr[i],arr[i//3]+1)
print(arr[N])
#
# if not i % 5:
#     arr[i] = min(arr[i], arr[i // 5] + 1)