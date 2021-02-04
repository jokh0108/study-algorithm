# 정수 삼각형

# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5


def solution(n, triangle):
    arr = [0] * (n + 1)
    for line in triangle:
        new_arr = arr[:]
        new_arr[0] += line[0]
        for i in range(1, len(line)):
            new_arr[i] = max(arr[i - 1], arr[i]) + line[i]
        arr = new_arr[:]
    return max(arr)


n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

print(solution(n, triangle))
