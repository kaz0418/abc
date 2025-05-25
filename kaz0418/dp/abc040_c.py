N = int(input())
A = list(map(int, input().split()))
C = [10**12 for i in range(N)]

# 配るDP
C[0] = 0
for i in range(0, N-2):
    C[i+1] = min(C[i+1], C[i]+abs(A[i+1]-A[i]))
    C[i+2] = min(C[i+2], C[i]+abs(A[i+2]-A[i]))

C[N-1] = min(C[N-1], C[N-2]+abs(A[N-1]-A[N-2]))

print(C[N-1])
