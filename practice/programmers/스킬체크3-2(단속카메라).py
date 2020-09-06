def solution(routes):
    LIMIT = 30000
    answer = len(routes)
    starts = {}
    ends = {}
    pos = LIMIT
    for idx, route in enumerate(routes):
        start, end = route
        if start < pos:
            pos = start
        if start not in starts:
            starts[start] = set([idx+1])
        else:
            starts[start].add(idx+1)
        if end not in ends:
            ends[end] = set([idx+1])
        else:
            ends[end].add(idx+1)
    print(starts)
    print(ends)
    print(pos)

    met = set(starts[pos])
    max_met = 1
    print(met)
    for n_pos in range(pos+1, LIMIT+1):
        if n_pos in starts:
            met = met | starts[n_pos]
            if max_met < len(met):
                max_met = len(met)
            print(n_pos, 'met', met)
        if n_pos in ends:
            met = met - ends[n_pos]
            print(n_pos, 'met', met)
        if not met:
            break
    return answer - max_met +1

print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
