def change_digits(t):
    new_t = []
    def change_digit(x):
        return '9' if x=='0' else str(int(x)-1)
    for x in t:
        new_t.append(change_digit(x))
    return ''.join(new_t)

s = input()
cnt = 0
while s != '':
    if s[-1] == '0':
        s = s[:-1]
        cnt += 1
    else:
        s = change_digits(s)
        cnt += 1

print(cnt)