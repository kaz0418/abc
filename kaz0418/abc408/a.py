N, S = map(int,input().split())
T = [0]+list(map(int,input().split()))
for i in range(N):
    if T[i+1] - T[i] > S + 0.5:
        print("No")
        exit()
print("Yes")