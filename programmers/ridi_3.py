def solution(arr):
    last_seen = {}
    min_days = float('inf')

    for i, customer_id in enumerate(arr):
        if customer_id in last_seen:
            days = i - last_seen[customer_id]
            min_days = min(min_days, days)
        last_seen[customer_id] = i

    return min_days if min_days != float('inf') else -1


# 테스트 케이스
print(solution([2, 1, 3, 1, 4, 2, 1, 3]))  # 예상 출력: 2
print(solution([1, 2, 3]))  # 예상 출력: -1
