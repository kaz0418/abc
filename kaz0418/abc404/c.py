# N, M = map(int, input().split())
# G = [[] for i in range(N)]

# for _ in range(M):
#     a, b = map(int, input().split())
#     G[a-1].append(b-1)
#     G[b-1].append(a-1)

# visited = [False for i in range(N)]

# now = 0

# before = -1

# visited = []

# for _ in range(N):
#     if len(G[now]) != 2:
#         print("No")
#         exit()

#     a, b = G[now]
#     next = a if before != a else b

#     visited.append(now)

#     if next == 0:
#         if len(visited) == N:
#             print("Yes")
#             exit()
#         print("No")
#         exit()

#     before = now
#     now = next

# UnionFindで解きなおし

from atcoder.dsu import DSU
# Cycle Graph判定は以下の二条件と同値
# 各点の次数が2
# すべての点が連結

N, M = map(int, input().split())
d = DSU(N)
cnt = [0]*N

for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    cnt[a] += 1
    cnt[b] += 1
    d.merge(a, b)

if all(c == 2 for c in cnt) and d.size(0) == N:
    print("Yes")
else:
    print("No")
