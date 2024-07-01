def solution(n):
    # 3의 거듭 제곱수 리스트 생성
    powers_of_three = []
    i = 0
    while 3 ** i <= 10 ** 10:
        powers_of_three.append(3 ** i)
        i += 1

    result = 0
    current_power = 0

    while n > 0:
        if n % 2 == 1:
            result += powers_of_three[current_power]
        n //= 2
        current_power += 1

    return result


# 예시 실행
print(solution(4))  # 9
print(solution(11))  # 31
