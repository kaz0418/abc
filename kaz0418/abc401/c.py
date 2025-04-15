import numpy as np

# メモ漸化式
n,k = map(int, input().split())

a = [0] * max(n+1,k)
for i in range(k):
    a[i] = 1
if n < k:
    print(1)
    exit()
a[k] = k
for i in range(k+1,n+1):
    a[i] = (2 * a[i-1] - a[i-k-1]) % (10**9)
print(a[n])

# 一般項から計算　→　浮動小数点エラー
# n,k = map(int,input().split())

# equation = [1]
# for i in range(k):
#     equation.append(-1)     # equation = [1, -1, -1, ... , -1] = lambda^k - lambda^{k-1} - ... - lambda -1 = 0

# lam = np.roots(equation)     # lambda_i

# a = 0
# if n > k:
#     for i in range(k):
#         prod = 1
#         for j in range(k):
#             if j != i:
#                 prod *= lam[i] - lam[j]
#         a += (np.power(lam[i],n) / prod) % 10**9
#     print(int(round(a))-10**9)

# if n <= k:
#     print(1)

# memo再帰 これもだめ
# n,k = map(int,input().split())
# def fib_memo(n,k,memo={}):
#     if n < k:
#         return 1
#     elif n in memo:
#         return memo[n]
#     else:
#         tmp = [fib_memo(i,k,memo) for i in range(n-k,n)]
#         return np.sum(tmp)%10**9

# print(fib_memo(n,k))

# a = []
# Simple_fibo おっそい
# for i in range(0,n+1):
#     if i < k:
#         a.append(1)
#     if i >= k:
#         a.append(np.sum(a[i-k:i]))
# print(a[-1])


