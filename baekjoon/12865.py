import sys
read = sys.stdin.readline

n, m = map(int, read().split())

dp = [0] * (m+1)

for i in range(n):
    w, v = map(int, read().split())

    for j in range(m, w-1, -1):
        dp[j] = max(dp[j], dp[j-w] + v)

print(max(dp))
