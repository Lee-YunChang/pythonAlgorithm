n, m = list(map(int, input().split()))
cards = list(map(int, input().split()))

sum = 0
for i in range(n-1):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            tmp = cards[i] + cards[j] + cards[k]

            if m >= tmp >= sum:
                sum = tmp

print(sum)
