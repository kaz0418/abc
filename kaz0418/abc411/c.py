N, Q = (map(int, input().split()))
A = list(map(int, input().split()))
B = [0 for i in range(N+1)]

s = 0
for i in range(Q):
    x = A[i]
    s += (1-2*B[x-1]) + (1-2*B[x])
    B[x-1] = (1-B[x-1])
    B[x] = (1-B[x])
    print(s//2)
