from collections import defaultdict

def solution(N, stages):
    trials = [0]*(N+2)
    onstage = [0]*(N+2)
    for stage in stages:
        if stage <= N:
            onstage[stage] += 1
        for i in range(stage):
            trials[i+1] += 1
    # print(trials, onstage)
    answer = []
    fail_rate = defaultdict(int)
    for i in range(1, N + 1):
        if trials[i] != 0:
            fail_rate[i] = onstage[i] / trials[i]
        else:
            fail_rate[i] = 0.0
    # print(fail_rate)
    answer = sorted(list(fail_rate.items()), key = lambda x : x[1], reverse=True)
    answer = [each[0] for each in answer]
    return answer
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
print(solution(500, [3]))