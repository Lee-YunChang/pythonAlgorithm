def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        filtered_skilltree = ''.join([c for c in skill_tree if c in skill])
        if is_valid_skill_tree(skill, filtered_skilltree):
            answer += 1

    return answer


def is_valid_skill_tree(skill, filtered_skilltree):
    for i in range(len(filtered_skilltree)):
        if skill[i] != filtered_skilltree[i]:
            return False
    return True