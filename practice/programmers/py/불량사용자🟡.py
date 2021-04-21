import collections
import itertools


def is_matched(string, pattern):
    if len(string) != len(pattern):
        return False
    for char1, char2 in zip(string, pattern):
        if char2 == "*":
            continue
        if char1 != char2:
            return False
    return True


def solution(user_ids, banned_ids):
    d = {}
    for banned_id in banned_ids:
        matched = list(filter(lambda x: is_matched(x, banned_id), user_ids))
        if banned_id in d:
            d[banned_id]["num"] += 1
        else:
            d[banned_id] = {"num": 1, "ids": matched}
    print(d)
    q = collections.deque()
    for v in d.values():
        r, ids = v["num"], v["ids"]
        new_q = collections.deque()
        if not q:
            for c in itertools.combinations(ids, r):
                new_q.append(set(c))
        else:
            while q:
                popped_set = q.popleft()
                for c in itertools.combinations(ids, r):
                    new_q.append(tuple(set(popped_set) | set(c)))
        q = new_q
    answer = 0
    for banned_set in q:
        if len(banned_set) == len(banned_ids):
            print("banned_set", sorted(banned_set))
            answer += 1
    return answer


print(
    solution(
        ["frodo", "frado", "fradi", "frxdi", "crodo", "qrkdo", "abc123", "frodoc"],
        ["fr*do", "fr*di", "*r*do", "******"],
    )
)
# print(
#     solution(
#         ["ㅁㄴ"],
#         ["**"],
#     )
# )
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
# print(
#     solution(
#         ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]
#     )
# )
# print(
#     solution(
#         ["frodo", "fradi", "crodo", "abc123", "frodoc"],
#         ["fr*d*", "*rodo", "******", "******"],
#     )
# )
