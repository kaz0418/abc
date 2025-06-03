from collections import deque

H, W = map(int, input().split())
table = [input() for i in range(H)]

# 初期の黒からの距離
dist = [[-1]*W for _ in range(H)]

# 黒の位置をキューに追加(開始地点は複数あってもよい)
blacks = deque()

for h in range(H):
    for w in range(W):
        if table[h][w] == '#':
            blacks.append((h, w))
            dist[h][w] = 0


def bfs(blacks, dist):
    d = 0
    while blacks:
        h, w = blacks.popleft()
        d = dist[h][w]
        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            new_h = h + dy
            new_w = w + dx
            if new_h < 0 or H <= new_h or new_w < 0 or W <= new_w:
                continue
            # セルが未探索なら
            if dist[new_h][new_w] == -1:
                # 隣りの黒の距離＋１
                dist[new_h][new_w] = d+1
                # 黒として登録
                blacks.append((new_h, new_w))
    return d


d = bfs(blacks, dist)
print(d)
