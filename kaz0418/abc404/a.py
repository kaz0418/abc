import string
S = input()
alphabets = string.ascii_lowercase
for a in alphabets:
    if a not in S:
        print(a)
        exit()
