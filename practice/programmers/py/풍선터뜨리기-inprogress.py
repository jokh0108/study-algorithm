def solution(arr):
    answer = 2
    x = [arr[0], arr[-1]]
    left_min = arr[0]
    right_set = set(arr[2:])
    right_min = min(right_set)
    print(right_set)
    print(arr)
    for i in range(1, len(arr)-1):
        print("left_min", left_min, "arr[i]", arr[i], "right_min", right_min)

        if left_min >= arr[i] or right_min >= arr[i]:
            x.append(arr[i])
            answer += 1
        left_min = min(left_min, arr[i])
        right_min = right_min if right_min == arr[i+1] else min(right_set)
        right_set.remove(arr[i+1])
        print(x, right_set)

    return answer


print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
