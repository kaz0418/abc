from itertools import combinations

N,L = map(int,input().split())
d = list(map(int,input().split()))

# 内接正三角形 ＝ 角が全て60度 ＝ π/3
# 円周はL
# 内接正三角形の各点を結んだこの長さはL/3

D = {0}
now = 0
for i in range(N-1):
    now = (now + d[i]) % L
    D.add(now)

cnt = 0
rad = L/3
for a, b, c in combinations(D, 3):
    d1 = abs(a-b) % L
    d2 = abs(b-c) % L
    d3 = abs(c-a) % L
    print(d1,d2,d3)
    if d1 == d2 and d2 == d3:
        cnt += 1

print(cnt)