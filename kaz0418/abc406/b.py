n, k = map(int, input().split())
A = list(map(int, input().split()))
prod = 1
for i in range(n):
    prod = prod*A[i] if prod*A[i] < 10**k else 1
print(prod)
