from sys import stdin

t = int(stdin.readline())

for i in range(t):

    n = int(stdin.readline())
    volunteers = []

    for j in range(n):
        volunteers.append(list(map(int, stdin.readline().split())))

    volunteers.sort()
    cnt = 0
    for k in range(len(volunteers)):
        if k == len(volunteers)-1:
            break

        if volunteers[k][1] > volunteers[k + 1][1]:
            cnt += 1

    print(cnt+1)
