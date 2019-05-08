def dfs(answer, numbers, target, cnt, M, summation, sign):
    # print(numbers[cnt], end=' ')
    if sign == '+':
        summation += numbers[cnt]
    elif sign == '-':
        summation -= numbers[cnt]
    if cnt != M:
        dfs(answer, numbers, target, cnt+1, M, summation, '+')
        dfs(answer, numbers, target, cnt+1, M, summation, '-')
    else:
        # print()
        # print(summation)
        if summation == target:
            answer.append(1)


def solution(numbers, target):
    answer = []
    summation = 0
    dfs(answer, numbers, target, 0, len(numbers)-1, summation, '+')
    dfs(answer, numbers, target, 0, len(numbers)-1, summation, '-')
    return len(answer)


print(solution([1, 1, 1, 1, 1], 3))
# print(solution([1, 2, 3, 4, 5], 3))
