def solution(skill, skill_trees):
    answer = 0
    for user_skill in skill_trees:
        sequence = ""
        for each in user_skill:
            if each in skill:
                sequence += each
        answer += 1
        for i in range(len(sequence)):
            if sequence[i] != skill[i]:
                answer -= 1
                break
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))