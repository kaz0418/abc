N, M = map(int,input().split())
wall = [0 for _ in range(N)] + [0]

# いもす法を使わない
# for _ in range(M):
#     L, R = map(int,input().split())
#     for i in range(L-1,R):
#         wall[i] += 1
# print(min(wall))

# いもす法
for _ in range(M):
    L, R = map(int,input().split())
    wall[L-1] += 1
    wall[R] -= 1

for i in range(1,N):
    wall[i] += wall[i-1]

print(min(wall[:-1]))