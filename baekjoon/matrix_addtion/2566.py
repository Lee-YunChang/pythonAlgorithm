
array = [list(map(int, input().split())) for _ in range(9)]
tmp = 0


for i in range(9):
    for j in range(9):
        array_value = array[i][j]
        if tmp <= array_value:
            tmp = array_value
            row = i + 1
            col = j + 1


print(tmp)
print(row, col)
