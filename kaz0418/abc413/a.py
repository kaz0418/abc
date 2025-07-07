n, m = (map(int, input().split()))
A = list((map(int, input().split())))
if m >= sum(A):
    print("Yes")
else:
    print("No")
