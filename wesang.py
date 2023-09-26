def solution(A):
    prev, diff = -1, 10 ** 9
    for a in (A):
        if prev != a:
            diff = min(diff, abs(a - prev))
        prev = a
    return diff

reps = [15, 11, 25]
result = solution(reps)
print(result)