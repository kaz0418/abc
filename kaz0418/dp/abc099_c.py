# DP
# n = int(input())
# memo = [i for i in range(n+1)]

# for i in range(n+1):
#     x = 6
#     while (0 <= i-x and x <= n):
#         tmp = memo[i-x]+1
#         memo[i] = tmp if tmp < memo[i] else memo[i]
#         x *= 6
#     x = 9
#     while (0 <= i-x and x <= n):
#         tmp = memo[i-x]+1
#         memo[i] = tmp if tmp < memo[i] else memo[i]
#         x *= 9

# print(memo[-1])

# memo再帰
n = int(input())
memo = [10**12 for i in range(n+1)]


def f(i):
    if n == 0:
        return 0
    if memo[i] != 10**12:
        return memo[i]

    res = 10**12
    cnt = f(i-1) + 1
    if cnt < res:
        res = cnt

    x = 6
    while (x <= i):
        cnt = f(i-x)+1
        if cnt < res:
            res = cnt
        x *= 6

    x = 9
    while (x <= i):
        cnt = f(i-x)+1
        if cnt < res:
            res = cnt
        x *= 9

    memo[i] = res
    return res


print(f(n))
