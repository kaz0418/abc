n, q = map(int,input().split())
X = list(map(int,input().split()))

B = [0]*n
min_idx = 1

for x in X:
    min_idx = B.index(min(B))+1

    if x == 0:
        B[min_idx-1] += 1
        print(min_idx,end=" ")
    else:
        B[x-1] += 1
        print(x, end=" ")