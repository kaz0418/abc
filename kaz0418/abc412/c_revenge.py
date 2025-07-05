from sys import stderr


def solve():
    N = int(input())
    S = list((map(int, input().split())))

    start = S[0]
    end = S[-1]

    # 二分探索(O(logn))をk回繰り返す
    # startミノの倍以下で最大のものを次のstartミノとして選ぶ
    # 個数がk個で最小となる並べ方が存在するとき、S[0] の2^k倍がS[-1]になる
    # (誤り)1<=S[i]<=10^9より、kは高々log2(10^9)~2^10^3=2^30
    # ↑一個先の大きさを2倍で近似してるけど、"高々"=上からの評価なので、
    # ここではkを上から抑えるため、「二個先のミノの大きさが2倍より大きい」を考える
    # (正しい) kは高々2log2(10^9)~60
    # n <= 2*10^5より、二分探索ならklogn < 60log(2*10^5)、全探索ならkn < 60*2*10^5

    # 全探索
    cnt = 2
    while start != end:
        if 2*start >= end:
            break
        m = start
        for s in S:
            if s <= 2*start:
                m = max(m, s)
        if m == start:
            print(-1)
            return
        start = m
        cnt += 1
    print(cnt)

    return


T = int(input())
for i in range(T):
    solve()
    print()
