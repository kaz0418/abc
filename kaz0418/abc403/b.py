import string
t = list(input())
U = input()
S = []

hatena_index = [i for i,x in enumerate(t) if x == '?']

for a in string.ascii_lowercase:
    for b in string.ascii_lowercase:
        for c in string.ascii_lowercase:
            for d in string.ascii_lowercase:
                t_ = t
                tmp = [a,b,c,d]
                for e,h in zip(tmp,hatena_index):
                    t_[h] = e
                S.append(''.join(t_))

for s in S:
    if U in s:
        print("Yes")
        exit()
print("No")