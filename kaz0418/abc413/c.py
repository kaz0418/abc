# メモリサイズがでかくなりすぎ？
# Q = int(input())

# A = []
# ptr = 0

# for i in range(Q):
#     q = list((map(int, input().split())))
#     if q[0] == 1:
#         for _ in range(q[1]):
#             A.append(q[2])
#     if q[0] == 2:
#         print(sum(A[ptr:ptr+q[1]]))
#         ptr = ptr + q[1]

# # キューでやってみる
# from collections import deque
# Q = int(input())

# A = deque()
# ptr = 0

# for _ in range(Q):
#     q = list((map(int, input().split())))
#     if q[0] == 1:
#         for _ in range(q[1]):
#             A.append((q[2]))
#     if q[0] == 2:
#         sum = 0
#         for _ in range(q[1]):
#             sum += A.popleft()
#         print(sum)

# from collections import deque
# Q = int(input())

# A = deque()
# ptr = 0

# for _ in range(Q):
#     q = list((map(int, input().split())))
#     if q[0] == 1:
#         for _ in range(q[1]):
#             A.append((q[2]))
#     if q[0] == 2:
#         sum = 0
#         for _ in range(q[1]):
#             sum += A.popleft()
#         print(sum)

# 最悪計算量はquery(2)の回数*Q
# →listを使う
# Q = int(input())

# A = []

# for _ in range(Q):
#     q = list((map(int, input().split())))
#     if q[0] == 1:
#         A.append([q[1], q[2]])
#     if q[0] == 2:
#         cnt = q[1]
#         sum = 0
#         while cnt != 0:
#             for i in range(len(A)):
#                 if cnt == 0:
#                     break
#                 if A[i][0] == 0:
#                     continue
#                 if cnt <= A[i][0]:
#                     sum += A[i][1] * cnt
#                     A[i][0] = A[i][0] - cnt
#                     cnt = 0
#                 if cnt > A[i][0]:
#                     sum += A[i][1] * A[i][0]
#                     cnt = cnt - A[i][0]
#                     A[i][0] = 0
#         print(sum)

from collections import deque

Q = int(input())
A = deque()

for _ in range(Q):
    q = list((map(int, input().split())))
    if q[0] == 1:
        A.append([q[1], q[2]])
    elif q[0] == 2:
        cnt = q[1]
        total = 0
        while cnt > 0:
            c, x = A[0]
            if cnt < c:
                total += x * cnt
                A[0][0] -= cnt
                cnt = 0
            else:
                total += x * c
                cnt -= c
                A.popleft()
        print(total)
