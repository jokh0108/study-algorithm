# 기타리스트


def solution(start, max_limit, volumes):
    volume_set = set([start])
    for volume in volumes:
        new_set = set()
        while volume_set:
            cur_volume = volume_set.pop()
            lower_volume, upper_volume = cur_volume - volume, cur_volume + volume
            if lower_volume >= 0:
                new_set.add(lower_volume)
            if upper_volume <= max_limit:
                new_set.add(upper_volume)
        volume_set = new_set.copy()

    if not volume_set:
        return -1
    return max(volume_set)


N, S, M = map(int, input().split())
V = map(int, input().split())

print(solution(S, M, V))
