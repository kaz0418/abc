from collections import deque

def minXorSumOfEdges(s, d, gr):
    dist = {node: float('infinity') for node in range(N+1)}
    dist[s] = 0
    
    # startとdestinationが一致
    if (s == d):
        return 0

    pq = []
    pq.append((0, s))

    # Visited array
    v = [0] * len(gr)

    while (len(pq) > 0):
        pq = sorted(pq)

        # Current node
        curr = pq[0][1]

        # Current xor sum of distance
        dist[curr] = pq[0][0]

        # Popping the top-most element
        del pq[0]

        # If already visited continue
        if (v[curr]):
            continue

        # Marking the node as visited
        v[curr] = 1

        # # If it is a destination node
        # if (curr == d):
        #     return dist

        # Traversing the current node
        for it in gr[curr]:
            pq.append((dist[curr] ^ it[1], it[0]))
            
    # If no path exists
    return dist[d] if dist[d] != float('infinity') else -1

# Driver code
if __name__ == '__main__':
    
    N, M = map(int,input().split())
    graph = [[] for i in range(N+1)]

    for _ in range(M):
        a, b, w = map(int,input().split())
        graph[a].append([b, w])

    print(minXorSumOfEdges(1, N, graph))