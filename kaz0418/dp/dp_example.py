# 最大和問題
# 1 <= n <= 10000
# -1000 <= a[i] <= 1000
# a[i]から何個かの整数を選んだ時の総和の最大値をdpで

import numpy as np

n = np.random.randint(1, 1001)
A = np.random.randint(-1000, 1001, n)

sum = 0
for a in A:
    if a > 0:
        sum += a

print("別解：", sum)


def chmax(dp, i, x):
    if dp[i] < x:
        dp[i] = x
        return True
    else:
        return False


def chmax(dp, i, x):
    if dp[i] < x:
        dp[i] = x
        return True
    return False


dp = [0] * (n+1)
# dp[i+1]はi番目までの整数から選んだ時の総和の最大値を入れる
# dp[0]はなにも選ばない時の値なので、0
# dp[n]が全ての整数から選んだ時の総和の最大値
for i in range(n):
    # if dp[i] < dp[i] + A[i]:
    #     dp[i+1] = dp[i] + A[i]
    # else:
    #     dp[i+1] = dp[i]
    chmax(dp, i+1, dp[i])
    chmax(dp, i+1, dp[i]+A[i])

print("dp：", dp[n])
