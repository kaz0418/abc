n = int(input())

ans = 0
for a in (2, 4):
    l = 0
    r = n
    while r-l > 1:
        m = (r+l)//2
        if a * m**2 <= n:
            l = m
        else:
            r = m
    ans += l

print(ans)
