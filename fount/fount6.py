def solution(n, m):
    answer = 0

    for i in range(n, m + 1):
        if is_palindrome(i):
            answer += 1

    return answer

def is_palindrome(num):
    original_num = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    return original_num == reversed_num

n = 1
m = 100

print(solution(n,m))