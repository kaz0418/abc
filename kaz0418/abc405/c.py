n = int(input())
A = list(map(int, input().split()))

# A1*A2 + A1*A3 + A2*A3 + ...
# A1*A2 + (A1+A2)*A3 + (A1+A2+A3)*A4 + ... + (A1+A2+...+An-1)*An

sum = A[0]
ans = 0
for i in range(1, n):
    ans += sum*A[i]
    sum += A[i]

print(ans)
