n, l = (map(int, input().split()))

if l % 3 != 0:
    print(0)
    exit()

D = list(map(int, input().split()))
P = {i: 0 for i in range(l)}

pos = 0
P[0] += 1
for i in range(n-1):
    pos = (pos+D[i]) % l
    P[pos] += 1

cnt = 0
for p in range(l//3):
    cnt += P[p] * P[(p+l//3) % l] * P[(p+2*l//3) % l]

print(cnt)
