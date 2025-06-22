n, k = (map(int, input().split()))
A = list(map(int, input().split()))

l = 0
r = n

while r > l:
    m = (r+l)//2
    if A[m] >= k:
        r = m
    else:
        l = m+1
if r == n:
    print(-1)
else:
    print(r)
