N = int(input())
D = list(map(int, input().split()))

for i in range(N-1):
    sum = 0
    for j in range(i, N-1):
        sum += D[j]
        print(sum, end=" ")
    print("")
