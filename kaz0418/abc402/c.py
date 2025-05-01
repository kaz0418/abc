import numpy as np
n,m = map(int,input().split())

A = []
menu = []
for _ in range(m):
    l = list(map(int,input().split()))
    k = l[0]
    tmp = 0
    for a in l[1:]:
        tmp += 1<<(a-1)
    menu.append(tmp)

# print("[ ",end="")
# for i in range(m):
#     print(bin(menu[i]),end=" ")
# print("]")

B = list(map(int,input().split()))
for b in B:
    tmp = 1<<(b-1)
    for i in range(m):
        menu[i] = menu[i] & ~tmp
    # print("克服",tmp,end=" ")
    # print("[ ",end="")
    # for i in range(m):
    #     print(bin(menu[i]),end=" ")
    # print("]")