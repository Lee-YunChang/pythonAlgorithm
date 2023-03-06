from sys import stdin

n, d = list(map(int, stdin.readline().split()))
m = 1
arr = [[0 for i in range(n)] for j in range(n)]

for i in range(n-d+1):
    for j in range(n):
        if j < n - d + 1:
            arr[i][j] = 0
        else:
            if m >= d:
                m = 1
            arr[i][j] = m
            m += 1

for i in range(n):
    for j in range(n-d+1, n):
        if m >= d:
            m = 1
        arr[j][i] = m
        m += 1

for i in arr:        # a에서 안쪽 리스트를 꺼냄
    for j in i:    # 안쪽 리스트에서 요소를 하나씩 꺼냄
        print(j, end=' ')
    print()
# for i in range(n):
#     for j in range(n):
#
#         if i < n-d+1:
#             if j < n-d+1:
#                arr[i][j] = 0
#             else:
#                 if m >= d:
#                     m = 1
#                 arr[i][j] = m
#                 m += 1
#         else:
#             if j < n-d+1:
#                arr[i][j] = 0
#             else:
#                 if m >= d:
#                     m = 1
#                 arr[j][i] = m
#                 m += 1
