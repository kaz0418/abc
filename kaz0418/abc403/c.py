# 愚直法　TLEなる
# 前回の苦手な食べ物の時みたいに逆引き作る？
# ユーザー数とページ数がどっちも2e5あるからきつそう
# 全ページアクセス可能ユーザーは-1って名前つけて検索回避
# setとlen使って全ページアクセス可能か判定したらTLE回避できた

n,m,q = map(int,input().split())

users = {}

for i in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        x = query[1]
        y = query[2]
        if x not in users:
            users[x] = {y}
        elif users[x] != -1:
            users[x].add(y)
            if len(users[x]) == m:
                users[x] = -1
    elif query[0] == 2:
        x = query[1]
        users[x] = -1
    elif query[0] == 3:
        x = query[1]
        y = query[2]
        if x not in users:
            print("No")
        elif users[x] == -1:
            print("Yes")
        else:
            if y in users[x]:
                print("Yes")
            else:
                print("No")