def solution(N, stages):
    stage_info = {i: [0, 0] for i in range(1, N+1)}
    print(stage_info)
    for st in stages:
        for i in range(1, st):
            stage_info[i][0] += 1
        if st <= N:
            stage_info[st][1] += 1
        print(stage_info)
    stage_info[N-1] = [0, 0]
    print(123, stage_info)
    fail_info = {k: v[1] / sum(v) if sum(v) != 0 else 0.0 for k, v in stage_info.items()}
    print(fail_info)
    answer = sorted([(stage, fail) for stage, fail in fail_info.items()], key=lambda x: x[1], reverse=True)
    print(answer)
    return [k for k, _ in answer]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
