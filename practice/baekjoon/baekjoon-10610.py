# 30
# 최대값이 10만자리가 될 수 있으므로 정수형이 아닌 문자형으로 받아야한다.


def solution(N):
    arr = list(map(int, list(N)))
    if not 0 in arr:
        return -1
    if sum(arr) % 3 != 0:
        return -1
    reversed_arr = sorted(list(map(int, str(N))), reverse=True)
    return int("".join(map(str, reversed_arr)))


# print(solution(input()))
print(solution("30"))
print(solution("102"))
print(solution("2913"))
print(solution("80875542"))
