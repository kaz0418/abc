from fractions import Fraction


def solve():
    N = int(input())
    A = list((map(int, input().split())))

    # すべて同じ値ならYes
    if A.count(A[0]) == N:
        return True

    # 公比-1を考慮(絶対値ソートだとNoになることがあるため)
    # ある項の1倍と-1倍がそれぞれceil(N/2)とfloor(N/2)ずつあり(1,-1,1のように同数でない場合もある)
    # Aの項がそれらだけに限られる
    pc = A.count(A[0])
    nc = A.count(-A[0])
    if min(pc, nc) == N//2 and pc + nc == N:
        return True

    abs_sorted_A = sorted(A, key=abs)
    r = Fraction(abs_sorted_A[1], abs_sorted_A[0])
    for i in range(len(abs_sorted_A)-1):
        if r != Fraction(abs_sorted_A[i+1], abs_sorted_A[i]):
            return False
    return True


T = int(input())
for _ in range(T):
    print("Yes" if solve() else "No")
