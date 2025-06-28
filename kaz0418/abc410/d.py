import heapq
from collections import defaultdict

def dijkstra(G,start,end):
    dist = {node: [2**10] for node in range(N+1)}
    dist[start].append(0)
    queue = [(start, 0)]
    
    while queue:
        now_node, now_dist = heapq.heappop(queue)

        for neighbor, weight in G[now_node]:
            d = now_dist ^ weight

            dist[neighbor].append(d)
            for d_ in dist[neighbor]:
                heapq.heappush(queue, (neighbor, d_))
    
    return min(dist[end]) if min(dist[end]) != 2**10 else -1

N, M = map(int,input().split())
G = defaultdict(list)

for _ in range(M):
    a, b, w = map(int,input().split())
    G[a].append((b,w))

print(dijkstra(G, 1, N))