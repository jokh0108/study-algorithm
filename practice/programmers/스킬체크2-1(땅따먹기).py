def findMax(line, before):
    M = 0
    cur = -1
    for i in range(len(line)):
        if line[i] > M and i != before:
            M = line[i]
            cur = i
    return M, cur

def solution(land):
    answer = 0
    before = -1
    
    for line in land:
        M, before = findMax(line, before)
        answer += M

    return answer

print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))