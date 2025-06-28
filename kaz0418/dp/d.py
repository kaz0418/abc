N, W = map(int, input().split())
values = []
weights = []

for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

# DFSでとけるらしいのでといてみる
# i番目以降の品物について、現在のリュックの重さがwであるときの価値の最大値をdfsで返す


# def dfs(i, w):
#     result = 0

#     # N番目以降の品物は存在しない
#     if i == N:
#         result = 0

#     # i番目(0~N-1)以降の品物について、リュックが開いていない時
#     elif w+weights[i] > W:
#         result = dfs(i+1, w)

#     # i番目(0~N-1)以降の品物について、リュックが開いているとき
#     else:
#         result = max(
#             # i番目の品物を入れなかったとき
#             # ->入れると価値が下がったりするかも
#             dfs(i+1, w),
#             # i番目の品物を入れたとき
#             dfs(i+1, w+weights[i])+values[i],
#         )

#     return result

# Memo再帰
dp = [[-1]*(W+1) for _ in range(N+1)]


def dfs(i, w):

    # 探索済み
    if dp[i][w] != -1:
        return dp[i][w]

    # N番目以降の品物は存在しない
    if i == N:
        result = 0

    # i番目(0~N-1)以降の品物について、リュックが開いていない時
    elif w+weights[i] > W:
        result = dfs(i+1, w)

    # i番目(0~N-1)以降の品物について、リュックが開いているとき
    else:
        result = max(
            # i番目の品物を入れなかったとき
            # ->入れると価値が下がったりするかも
            dfs(i+1, w),
            # i番目の品物を入れたとき
            dfs(i+1, w+weights[i])+values[i],
        )
    dp[i][w] = result
    return result


print(dfs(0, 0))
