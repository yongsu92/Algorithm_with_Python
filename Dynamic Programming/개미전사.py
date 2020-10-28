N = 4
arr = [1,3,1,5]
check = [0]*101
check[1] = arr[1]
for i in range(2,N+1):
    check[i] = max(check[i-2]+arr[i-1],check[i-1])
print(check[N])