def solution(array, commands):
    answer = []
    for command in commands:
        cut = array[command[0]-1:command[1]]
        answer.append(sorted(cut)[command[2]-1])
    return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])