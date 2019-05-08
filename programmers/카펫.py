def solution(brown, red):
    x1 = ((brown + 4) + ((brown + 4) ** 2 - 16 * (brown + red)) ** 0.5) // 4
    y1 = (brown + red) // x1
    x2 = ((brown + 4) - ((brown + 4) ** 2 - 16 * (brown + red)) ** 0.5) // 4
    y2 = (brown + red) // x2
    print(x1, y1, x2, y2)
    if x1 < y1:
        x1 = x2
        y1 = y2
    return [int(x1), int(y1)]

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))