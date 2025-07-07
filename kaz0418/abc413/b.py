N = int(input())
S = []
res = []

for _ in range(N):
    S.append(input())

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        tmp = S[i] + S[j]
        if tmp not in res:
            res.append(tmp)

print(len(res))
