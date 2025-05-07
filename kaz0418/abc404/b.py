import copy
N = int(input())
S = []
T = []
for i in range(N):
    S.append(list(input()))
for i in range(N):
    T.append(list(input()))

def rotate(S):
    S_rotated = [["." for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            S_rotated[j][N-i-1] = S[i][j]
    return S_rotated

min_cnt = N*N

print(min_cnt)

