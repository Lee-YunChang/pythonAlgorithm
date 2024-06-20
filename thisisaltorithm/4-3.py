

n, m = map(int, input().split())

x, y, look = map(int, input().split())

map_arr = [list(map(int, input().split())) for _ in range(n)]
temp_arr = [[0] * m for _ in range(n)]

count = 1
temp_arr[x][y] = 1





print(map_arr)
print(temp_arr)


# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1
