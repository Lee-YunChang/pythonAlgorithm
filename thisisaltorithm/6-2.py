
n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))


tmp_arr = []
for j in range(len(arr)):
    if (arr[j] < arr[j+1]):
        tmp_arr.append(arr[j+1])


print(tmp_arr)
