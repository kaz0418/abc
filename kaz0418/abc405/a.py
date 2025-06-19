r, x = (map(int, input().split()))
th = {1: (1600, 3000), 2: (1200, 2400)}

if th[x][0] <= r < th[x][1]:
    print("Yes")
else:
    print("No")
