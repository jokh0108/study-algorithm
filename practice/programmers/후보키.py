import itertools


def does_smaller_exists(combination, candidates):
    for candidate in candidates:
        if set(candidate).issubset(set(combination)):
            return True
    return False


def solution(relation):
    candidates = set()
    for i in range(1, len(relation[0])+1):
        for c in itertools.combinations(range(len(relation[0])), i):
            if does_smaller_exists(c, candidates):
                continue
            keys = set([tuple(row[v] for v in c) for row in relation])
            # print(len(relation), len(keys), c, keys)
            if len(relation) == len(keys):
                candidates.add(c)
                # print(candidates)
    return len(candidates)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
print(solution([["a", "1", "4"], ["2", "1", "5"], ["a", "2", "4"]]))
print(solution([["a", "b", "c"], ["1", "b", "c"], ["a", "b", "4"], ["a", "5", "c"]]))
print(solution([["100", "ryan", "music", "2"]]))
