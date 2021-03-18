def solution(distance, rocks, n):
    rocks = sorted(rocks)
    points = [0, *rocks, distance]
    # print(points)
    intervals = [points[i+1] - points[i] for i in range(len(points)-1)]
    # print("intervals", intervals)
    sorted_intervals = sorted([(v, i) for i, v in enumerate(intervals)])
    # print("sorted_intervals", sorted_intervals)
    targets = [i for _, i in sorted_intervals[:n]]
    # targets = sorted([i for _, i in sorted_intervals[:n]], reverse=True)
    # print("targets", targets)
    for target in targets:
        if target == 0:
            intervals[1] += intervals[0]
        elif target == len(intervals)-1:
            intervals[-2] += intervals[-1]
        else:
            if intervals[target+1] < intervals[target-1]:
                intervals[target+1] += intervals[target]
            else:
                intervals[target-1] += intervals[target]

        # print(intervals)
    targets_set = set(targets)
    new_intervals = [x for i, x in enumerate(
        intervals) if i not in targets_set]
    # print(new_intervals)

    return min(new_intervals)


print(solution(25, [2, 14, 11, 21, 17], 2))
