def solution(numbers, hand):

    KEYPAD = {
        1:   (0, 0),   2: (0, 1), 3:   (0, 2),
        4:   (1, 0),   5: (1, 1), 6:   (1, 2),
        7:   (2, 0),   8: (2, 1), 9:   (2, 2),
        "*": (3, 0),   0: (3, 1), "#": (3, 2),
    }

    left, right, result = "*", "#",  ""

    for n in numbers:
        if n in {1, 4, 7}:
            result += "L"
            left = n
        elif n in {3, 6, 9}:
            result += "R"
            right = n
        else:
            (x1, y1), (x2, y2), (x3, y3) =\
                KEYPAD[left], KEYPAD[right], KEYPAD[n]
            left_distance = abs(x3-x1) + abs(y3-y1)
            right_distance = abs(x3-x2) + abs(y3-y2)

            result += "L"
            prev_left = left
            left = n
            if left_distance > right_distance or\
                    left_distance == right_distance and hand == "right":
                result = result[:-1] + "R"
                right = n
                left = prev_left
    return result


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
