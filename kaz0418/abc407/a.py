a,b = map(int,input().split())
d = a/b
i = a//b
print(i if abs(i-d) < abs(i+1-d) else i+1)