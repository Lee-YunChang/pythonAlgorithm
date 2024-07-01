def solution(arr, n):
    seen = set()
    for num in arr:
        if n - num in seen:
            return True
        seen.add(num)
    return False

# 예시 테스트
arr1 = [5, 3, 9, 13]
n1 = 8
print(solution(arr1, n1))  # 예: True

arr2 = [5, 3, 9, 13]
n2 = 7
print(solution(arr2, n2))  # 예: False
