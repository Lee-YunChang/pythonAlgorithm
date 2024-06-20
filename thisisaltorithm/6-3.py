

n = int(input())

arr = []
for i in range(n):
    data = input().split()
    arr.append((data[0], int(data[1])))

arr = sorted(arr, key=lambda score:score[1])

for score in arr:
    print(score[0])
