def is_beautiful(arr):
    print(arr)
    for i in range(1, len(arr)-1):
        if (arr[i] - arr[i-1]) * (arr[i+1] - arr[i]) >= 0:
            return False
    return True


def solution(arr):
    cnt = 0
    if is_beautiful(arr):
        return cnt
    for i in range(len(arr)):
        if is_beautiful([arr[j] for j in range(len(arr)) if j != i]):
            cnt += 1
    if not cnt:
        return -1
    return cnt


print(solution([3, 4, 5, 3, 7]))
print(solution([1, 2, 3, 4]))
print(solution([1, 3, 1, 2]))