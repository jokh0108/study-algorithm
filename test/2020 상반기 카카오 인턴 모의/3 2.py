import itertools
import copy

def is_matchable(user, banned):
    if len(user) != len(banned):
        return False
    for i in range(len(user)):
        if banned[i] == '*':
            continue
        elif user[i] == banned[i]:
            continue
        else:
            return False
    return True

def solution(user_id, banned_id):
    answer = 0
    matched = {}
    for b in banned_id:
        if b not in matched:
            matched[b] = [1, set()]
        else:
            matched[b][0] += 1
    print(matched)

    for b in banned_id:
        for u in user_id:
            if is_matchable(u, b):
                matched[b][1].add(u)
    print(matched)
    cases = [set()]
    print(cases)
    new_cases = []
    for n, user_ids in matched.values():
        for c in itertools.combinations(user_ids, n):
            for i in range(len(cases)):
                new_cases.append(cases[i].union(set(c)))
        cases = copy.deepcopy(new_cases)
        new_cases = []
        print(cases)
    for case in cases:
        if len(case) == len(banned_id):
            answer += 1
    return answer


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
