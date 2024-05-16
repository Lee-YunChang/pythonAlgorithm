from sys import stdin

k = int(stdin.readline())

lines = []
for i in range(k):
    lines.append(list(map(int, stdin.readline().split())))
lines.sort(key=lambda x: x[0])

length =[]

min_length = lines[0][0]
for i in range(1, len(lines)):

    if lines[i][0] >= lines[i-1][1]:
        length.append([min_length, lines[i-1][1]])
        min_length = lines[i][0]

    if i == len(lines)-1:
        length.append([min_length, lines[i][1]])

long = 0
for i in range(len(length)):
    long += length[i][1]-length[i][0]

print(long)


