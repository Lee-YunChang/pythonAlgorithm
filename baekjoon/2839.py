from sys import stdin
n = int(stdin.readline())
output = -1
for i in range(int(n/3)+1):
    a = n-(i*3)
    if a % 5 == 0:
        output = i + (a / 5)
        break
print(int(output))
