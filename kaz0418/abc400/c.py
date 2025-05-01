import numpy as np
N = int(input())

cnt = 0
ans = 0
for a in [1,2]:
    l = 1
    r = N
    # 2**a * b**2 が N を超えない最大の整数 b を探す
    # 二分探索
    while l+1 < r:
        m = (l+r)//2
        x = (2**a)*(m**2) 
        if x <= N:
            l = m
        else:
            r = m
    ans += l
print(ans)


# b^2のカウントを愚直にやるとTLE
# for i in range(1,3):
#     for j in range(1,N//(2**i)+1):
#         if (2**i) * j**2 > N:
#             continue
#         cnt += 1
#         # print((2**i)*j**2)

# print(cnt)
