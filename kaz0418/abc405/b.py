n, m = (map(int, input().split()))
A = list(map(int, input().split()))

cnt = 0
# 1以上m以下のセット
B = set(range(1, m+1))

cnt = 0
for i in range(n+1):
    if set(A[0:n-i]) < B:
        print(cnt)
        break
    cnt += 1
