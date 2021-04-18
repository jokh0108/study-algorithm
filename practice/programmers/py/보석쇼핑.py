# 한 3~4시간 걸렸나 겨우 풀어낸 문제같다.
# 방법은 맞았는데 코딩이 문제였다.
# i, j 투포인터(혹은 슬라이드 윈도우)를 어느 조건마다 하나씩 옮겨야 했는데
# 하나씩 컨트롤 하려고 하니 문제가 너무 어려워졌다.
# 처음에는 while문으로 i, j를 둘 다 0으로 두고 하나씩 더해갔다.
# 그러다 보니 j가 index out of range가 되거나
# i 가 제대로 반영이 되지 않는 등 여러가지 문제가 생겼다.

# 그래서 j를 for 문으로 돌려서 자동으로 움직이게 하고,
# 조건에 해당될떄(len(counter) == kinds)만 i를 움직이도록 했다.
# 조건을 최소화 하도록 한 것이다.

import collections


def solution(gems):
    kinds = len(set(gems))
    answer = [1, len(gems)]
    counter = collections.Counter()
    interval = len(gems)
    i = 0
    for j, gem in enumerate(gems):
        counter[gem] += 1
        if len(counter) == kinds:
            while i < j and counter[gems[i]] > 1:
                counter[gems[i]] -= 1
                if counter[gems[i]] == 0:
                    del counter[gems[i]]
                i += 1
            print(333, i, j, gems[i : j + 1], counter)
            if interval > j - i + 1:
                interval = j - i + 1
                print("kkk", interval)
                if interval == kinds:
                    return [i + 1, j + 1]
                answer = [i + 1, j + 1]

        print(444, i, j, gems[i : j + 1], counter)

    return answer


# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(
    solution(
        [
            "a",
            "a",
            "a",
            "b",
            "b",
            "c",
            "d",
            "b",
            "c",
            "b",
            "a",
            "b",
            "c",
            "d",
            "a",
            "a",
            "b",
            "d",
        ]
    )
)
# print(solution(["DIA", "DIA"]))
# print(
#     solution(
#         ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
#     )
# )
# print(
#     solution(
#         ["AA", "AB", "AC", "AA", "AC"],
#     )
# )
# print(
#     solution(
#         ["XYZ", "XYZ", "XYZ"],
#     )
# )
# print(
#     solution(
#         ["ZZZ", "YYY", "NNNN", "YYY", "BBB"],
#     )
# )

# O(n^2) solution
# max_num = len(set(gems))
# min_length = len(gems)
# interval = [1, len(gems)+1]

# for i in range(len(gems)):
#     for j in range(len(gems)):
#         current_num = len(set(gems[i:j+1]))
#         print(gems[i], gems[j], set(gems[i:j+1]))
#         if current_num == max_num and min_length > j-i:
#             min_length = j-i
#             interval = [i+1, j+1]
#             print("interval", interval)
# return interval
