a, b, c, d = map(int, input().split())
if c < a:
    print("Yes")
    exit()
elif c == a:
    if d < b:
        print("Yes")
        exit()
print("No")
