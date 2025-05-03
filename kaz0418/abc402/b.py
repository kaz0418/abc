from collections import deque

q = int(input())

queue = deque([])
for _ in range(q):
    query = tuple(map(int,input().split()))
    if query[0] == 1:
        queue.append(query[1])
    if query[0] == 2:
        print(queue.popleft())
