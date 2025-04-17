N=int(input())
m = ""
if N%2==0:
    s = "=="
else:
    s = "="
for i in range((N-len(s))//2):
    m = m + "-" 
print(m + s + m)
