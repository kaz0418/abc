N,Q = map(int,input().split())
A = [i+1 for i in range(N)] # 1-index

# 先頭を表すポインタ
head = 0

for _ in range(Q):
    q = list(map(int,input().split()))

    if q[0] == 1:
        p = (head + q[1] - 1) % N
        A[p] = q[2]

    elif q[0] == 2:
        p = (head + q[1] - 1) % N
        print(A[p])

    elif q[0] == 3:
        head = (head + q[1])%N
    