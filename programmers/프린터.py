def solution(priorities, location):
    answer = 0
    max_priority = max(priorities)
    while True:
        #break
        #print(deq)
        current = priorities.pop(0)
        if current != max_priority:
            priorities.append(current)
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1
        else:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            max_priority = max(priorities)
    #print(answer)
    return location

solution([2, 1, 3, 2], 2)
print()
solution([1, 1, 9, 1, 1, 1], 0)