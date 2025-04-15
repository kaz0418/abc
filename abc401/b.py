N = int(input())
S = []
state = "logout"

def authorize(state,acction):
    if state == "logout" and acction == "private":
        return 1
    return 0

def changeState(state,acction):
    if acction == "login":
        state = "login"
    elif acction == "logout":
        state = "logout"
    return state

cnt = 0
for _ in range(N):
    acction = input()
    state = changeState(state,acction)
    cnt += authorize(state,acction)

print(cnt)