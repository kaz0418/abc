n = int(input())
a_list = list(map(int,input().split()))
sum = 0
for i in range(0,len(a_list),2):
    sum += a_list[i]
print(sum)