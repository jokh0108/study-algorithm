from itertools import combinations, permutations


def solution(baseball):
    digits = set(map(str, range(1, 10)))
    case = []
    for each in baseball:
        s = set()
        num = list(str(each[0]))
        strike = each[1]
        ball = each[2]
        for comb in combinations(range(3), strike):
            restIndex = list(set(range(3))-set(comb))
            for temp in combinations(restIndex, ball):
                temp = set(temp)
                for other in permutations(digits.difference(set(comb)), 3 - strike):
                    flag = True
                    for j in range(len(restIndex)):
                        if num[restIndex[j]]==other[j]:
                            flag = False
                    if set(other).issuperset(set([num[i] for i in temp])) & flag:
                        possible = [0]*3
                        for i in comb:
                            possible[i] = num[i]
                        for i in range(len(restIndex)):
                            possible[restIndex[i]] = other[i]
                        # print()
                        s.add(int("".join(possible)))
#                         # print(comb + other)
        case.append(s)
    answer = case[0]
    for each in case:
        # print(sorted(list(each)))
        answer = answer.intersection(each)
    return len(answer)


# print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))
# print(solution([[327, 2, 0], [123, 1, 1], [356, 1, 0],[489, 0, 1]]))
# print(solution([[123, 3, 0]]))
