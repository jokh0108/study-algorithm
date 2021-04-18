def get_len_of_longest_hole(arr):
    max_hole_len = 0
    hole_len = 0
    for value in arr:
        if value == 0:
            hole_len += 1
            max_hole_len = max(max_hole_len, hole_len)
        else:
            hole_len = 0
    return max_hole_len


def solution(stones, k):
    maximum, left_step, right_step = 1, 1, 200_000_000
    while left_step <= right_step:
        step = (left_step + right_step) // 2
        stones_crossed = list(map(lambda x: x - step if x - step > 0 else 0, stones[:]))
        max_hole_len = get_len_of_longest_hole(stones_crossed)
        print(left_step, step, right_step, stones_crossed, max_hole_len)
        if max_hole_len < k:
            left_step = step + 1
            maximum = max(maximum, step + 1)
        else:
            right_step = step - 1

    return maximum


# print("answer: ", solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
# print("answer: ", solution([2, 4, 5], 3))
# print("answer: ", solution([2, 4, 5], 3))
print("answer: ", solution([2, 3, 10, 3], 2))
