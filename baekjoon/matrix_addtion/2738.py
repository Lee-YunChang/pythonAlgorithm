

n, m = map(int, input().split())

arr_a = [list(map(int, input().split())) for _ in range(n)]
arr_b = [list(map(int, input().split())) for _ in range(n)]

result = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(arr_a[i][j] + arr_b[i][j])
    result.append(row)


for row in result:
    print(' '.join(map(str, row)))

