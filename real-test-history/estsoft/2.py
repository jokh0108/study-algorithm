from collections import defaultdict

def solution(arr):
    d = defaultdict(list)
    for a in arr:
        digit_sum = 0
        aa = a
        while aa:
            digit_sum += aa % 10
            aa = aa // 10
        if not d[digit_sum]:
            d[digit_sum] = []
        if len(d[digit_sum]) < 2:
            d[digit_sum].append(a)
        else:
            idx = d[digit_sum].index(min(d[digit_sum]))
            if d[digit_sum][idx] < a:
                d[digit_sum][idx] = a
    for lst in d.values():
        if len(lst) != 2:
            return -1
    print(d)
    return max(sum(l) for l in d.values())


print(solution([51, 71, 17, 42]))
print(solution([42, 33, 60]))
print(solution([51, 32, 43]))