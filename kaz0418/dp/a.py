n = int(input())
H = list(map(int, input().split()))
C = [0 for i in range(n)]
C[0] = 0
C[1] = abs(H[0]-H[1])
for i in range(2, n):
    C[i] = min(C[i-2]+abs(H[i]-H[i-2]), C[i-1]+abs(H[i]-H[i-1]))
print(C[-1])
