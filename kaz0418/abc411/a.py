import sys
P = input()
L = int(input())

# デバッグ出力はstderrを使う
# sys.stderr.write(P)

if len(P) >= L:
    print("Yes")
else:
    print("No")
