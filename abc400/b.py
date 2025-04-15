n,m = map(int,input().split(' '))
x = 0

for i in range(m+1):
    x += n**i
if x <= 10**9:
    print(x)
else:
    print("inf")