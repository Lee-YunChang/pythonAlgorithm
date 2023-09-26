def solution(no, works):
    if sum(works) <= no:
        return 0

    while no > 0:
        max_work = max(works)
        max_indices = [i for i, x in enumerate(works) if x == max_work]

        for index in max_indices:
            if no == 0:
                break
            works[index] -= 1
            no -= 1

    return sum([i * i for i in works])


no = 2
works = [3,3,3]
print(solution(no, works))