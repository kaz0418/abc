N = int(input())
A = list(map(int,input().split()))

A.sort()
max_x = 0

l = 0
r = A[-1]

while l <= r:
    x = (l + r) // 2

    cnt = 0
    for i in range(N):
        if A[i] >= x:
            cnt += 1
    if cnt >= x:
        max_x = x
        l = x+1
    else:
        r = x-1

print(max_x)