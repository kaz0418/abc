S = input()+'0'
cnt = 0
for i in range(0, len(S)-1):
    cnt += (int(S[i])-int(S[i+1])) % 10
print(cnt+len(S)-1)
