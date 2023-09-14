def multiple_knapsack_maximize_weight(weights, capacities):
    k = len(capacities)  # 배낭의 개수
    max_weights = [0] * k  # 각 배낭의 최대 무게

    for i in range(k):
        capacity = capacities[i]
        n = len(weights)  # 물건의 개수
        dp = [0] * (capacity + 1)

        for j in range(n):
            for w in range(capacity, 0, -1):
                if weights[j] <= w:
                    dp[w] = max(dp[w], dp[w - weights[j]] + weights[j])

        max_weights[i] = dp[capacity]

    return max_weights


# 테스트용 입력 데이터
weights = [1, 2, 3, 4, 5]
capacities = [5, 5]
result = multiple_knapsack_maximize_weight(weights, capacities)
print("최대 갯수:", result)