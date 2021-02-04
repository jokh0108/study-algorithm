import pprint
import itertools
import collections

def solution(orders, course):
    answer = []
    for num in course:
        d = collections.defaultdict(int)
        for order in orders:
            for combination in itertools.combinations(order, num):
                # print(combination, order, num)
                d[tuple(sorted(combination))] += 1
        # pprint.pprint(list(d.items()))
        if not d:
            continue
        max_count = max(d.values())
        # print(max_count)
        answer.extend(["".join(combination) 
                            for combination, count in d.items() 
                            if count == max_count and count >= 2])
    # print(answer)
    return sorted(answer)

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))