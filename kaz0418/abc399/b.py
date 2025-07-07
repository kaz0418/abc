N = int(input())
P = list((map(int, input().split())))
R = [0 for i in range(N)]
r = 1

while 0 in R:
    max_x = 0
    k = 0
    for i in range(N):
        if R[i] != 0:
            continue
        if max_x < P[i]:
            max_x = P[i]
    for j in range(N):
        if R[j] != 0:
            continue
        if P[j] == max_x:
            R[j] = r
            k += 1
    r = r+k

for i in range(N):
    print(R[i])
