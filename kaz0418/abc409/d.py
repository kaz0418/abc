def solve():
    N = int(input())
    S = input()
    head = 0
    for i in range(N-1):
        if S[i] > S[i+1]:
            head = i
            break
    S_ = S[0:head] + S[head+1:]
    head_s = S[head]
    for i in range(0, N-1):
        if head_s < S_[i]:
            return S_[0:i] + head_s + S_[i:]
    return S_[0:N-1] + head_s


T = int(input())
for _ in range(T):
    print(solve())
