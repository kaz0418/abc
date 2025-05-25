n, k = map(int, input().split())
h = list(map(int, input().split()))
c = [10**12 for i in range(n)]

# rangeの範囲に注意
for i in range(min(n, k+1)):
    c[i] = abs(h[i]-h[0])

for i in range(n):
    for j in range(1, min(i, k+1)):
        cost = abs(h[i]-h[i-j]) + c[i-j]
        c[i] = cost if cost < c[i] else c[i]

print(c[-1])
