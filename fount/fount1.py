def solution(cookie):
    N = len(cookie)
    sum_list = [0] * (N + 1)

    for i in range(N):
        sum_list[i + 1] = sum_list[i] + cookie[i]

    max_number = 0

    for l in range(1, N):
        for m in range(l, N):
            for r in range(m + 1, N + 1):
                left_sum = sum_list[m] - sum_list[l - 1]
                right_sum = sum_list[r] - sum_list[m]

                if left_sum == right_sum:
                    max_number = max(max_number, max(cookie[l:m + 1] + cookie[m + 1:r]))

    return max_number

cookie = [1, 1, 2, 3]
result = solution(cookie)

print(result)