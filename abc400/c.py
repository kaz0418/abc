import numpy as np
N = int(input())

cnt = 0
for i in range(1,3):
    for j in range(1,N//(2**i)+1):
        if (2**i) * j**2 > N:
            continue
        cnt += 1
        # print((2**i)*j**2)

print(cnt)
