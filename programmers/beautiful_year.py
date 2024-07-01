def solution(p):
    def is_beautiful_year(year):
        year_str = str(year)
        return len(set(year_str)) == len(year_str)

    year = p + 1
    while True:
        if is_beautiful_year(year):
            return year
        year += 1


# 예시 테스트
p = 9998
print(solution(p))  # 예: 10234 (또는 그 이후의 첫 아름다운 연도)
