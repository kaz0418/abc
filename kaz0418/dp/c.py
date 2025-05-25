n = int(input())
happy = [[0, 0, 0] for i in range(n+1)]


def chmax(DP, i, j, v):
    if DP[i][j] <= v:
        DP[i][j] = v


for i in range(n):
    actions = list(map(int, input().split()))
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            today_happy = happy[i][j] + actions[k]
            chmax(happy, i+1, k, today_happy)

print(max(happy[-1]))
