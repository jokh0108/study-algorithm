import collections


def solution(gems):
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
    counter = collections.Counter(gems)
    print(counter)
    i, j = 0, len(gems)-1
    while counter[gems[j]] - 1 > 0:
        counter[gems[j]] -= 1
        j -= 1
    while counter[gems[i]] - 1 > 0:
        counter[gems[i]] -= 1
        i += 1
    return [i+1, j+1]


print(solution(["DIA", "RUBY", "RUBY", "DIA",
                "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
