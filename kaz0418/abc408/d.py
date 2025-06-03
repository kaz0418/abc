def min_operations(S):
    # 1の出現位置を記録
    ones = [i for i, ch in enumerate(S) if ch == '1']
    total = len(ones)
    if total == 0:
        return 0  # 全て0なら操作不要

    # 累積和（各位置の合計）を取る
    prefix = [0] * (total + 1)
    for i in range(total):
        prefix[i + 1] = prefix[i] + ones[i]

    res = total  # 最悪は全て1を0にする
    for k in range(1, total + 1):  # 長さkの1区間を作る
        for i in range(total - k + 1):
            j = i + k - 1
            mid = i + k // 2
            median = ones[mid]

            # 中央にそろえるときの移動距離の合計を求める
            left = median * (mid - i) - (prefix[mid] - prefix[i])
            right = (prefix[j + 1] - prefix[mid + 1]) - median * (j - mid)
            cost = left + right
            res = min(res, cost)

    return res

T = int(input())

for _ in range(T):
    N = input()
    S = input()
    print(min_operations(S))
    