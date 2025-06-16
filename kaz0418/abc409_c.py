from collections import defaultdict
N, L = map(int, input().split())
D = list(map(int, input().split()))

t = 0

# defaultdictの中には初期化関数を入れる
# intと書くのは、lambda: intと書くのと同じで、0で初期化になるらしい
# lambda: 1とかけば1で初期化
points = defaultdict(int)
points[0] = 1

for i in range(N-1):
    t = (t + D[i]) % L
    points[t] += 1

P = sorted(points)
cnt = 0

for i in range(0, len(P)):
    p1 = P[i]
    if p1 > L/3:
        break
    p2 = p1 + L/3
    p3 = p2 + L/3
    cnt += points[p1] * points[p2] * points[p3]

print(cnt)
