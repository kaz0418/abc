def solve(n, s):
    # n = int(input())
    # s = input()

    # 1の累積和をとる
    sum_ones = [0 for _ in range(n+1)]
    sum_zeros = [0 for _ in range(n+1)]
    for i in range(n):
        sum_ones[i+1] = sum_ones[i] + (1 if s[i] == '1' else 0)
        sum_zeros[i+1] = sum_zeros[i] + (1 if s[i] == '0' else 0)

    # 累積和の確認
    # print(sum_ones)

    # caseの真ん中に1をそろえる(1の区間の左端をl、右端をrとする)
    # 解はlより左の1の数とl,rの真ん中の0の数と、rより右の1の個数の和
    for l in range(0, n):
        for r in range(1, n+1):


case = "1011011101"
solve(len(case), case)
