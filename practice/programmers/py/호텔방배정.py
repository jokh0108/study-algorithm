def solution(k, room_numbers):
    # # 효율성 탈락
    # answer = []
    # s = set()
    # for room_number in room_numbers:
    #     if room_number in s:
    #         while room_number in s:
    #             room_number += 1
    #     s.add(room_number)
    #     answer.append(room_number)
    # return answer
    assigned = {}
    answer = []
    for room_number in room_numbers:
        if room_number in assigned:
            nodes = [room_number]
            while room_number in assigned:
                room_number = assigned[room_number]
                nodes.append(room_number)
            for node in nodes:
                assigned[node] = room_number + 1
        assigned[room_number] = room_number + 1
        print(assigned)
        answer.append(room_number)
    return answer


# print(solution(10, [1, 3, 1, 1]))

print(solution(10, [1, 3, 4, 1, 3, 1]))
