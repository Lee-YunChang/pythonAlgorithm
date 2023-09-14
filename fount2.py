def min_score_difference(grade):
    origin_grade_sum = sum(grade)

    for i in reversed(range(1, len(grade))):
        if grade[i] > grade[i-1]:
            continue
        else:
            grade[i-1] = grade[i]

    sorted_grade_sum= sum(grade)

    return origin_grade_sum - sorted_grade_sum


# Example usage:
grade = [3, 2, 3, 6, 4, 5]
result = min_score_difference(grade)
print(result)