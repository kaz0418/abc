N, M = map(int, input().split())
G = [[] for i in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

visited = [False for i in range(N)]

now = 0

before = -1

visited = []

for _ in range(N):
    if len(G[now]) != 2:
        print("No")
        exit()

    a, b = G[now]
    next = a if before != a else b

    visited.append(now)

    if next == 0:
        if len(visited) == N:
            print("Yes")
            exit()
        print("No")
        exit()

    before = now
    now = next
