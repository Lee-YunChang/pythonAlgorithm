def solution(phrase):
    color_type = {'red': [], 'green': []}  # 딕셔너리 값에 대괄호를 사용하여 빈 리스트로 초기화

    is_red = True
    for char in phrase:
        if char == ' ':
            continue

        color = 'red' if is_red else 'green'
        is_red = not is_red
        if char not in color_type[color]:
            color_type[color].append(char)

    answer = len(color_type['red']) + len(color_type['green'])  # 딕셔너리 키를 올바르게 사용
    return answer


# 예시: "HELLO WORLD" 문구를 만들기 위해 필요한 양초 종류 수 계산
phrase = "HELLO WORLD"
result = solution(phrase)
print(result)  # 출력: 8
