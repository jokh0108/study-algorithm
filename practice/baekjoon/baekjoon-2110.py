# 공유기 설치
# 집의 좌표를 대상으로 binary search인 줄 알았으나
# 간격을 대상으로 하는게 반전인 문제.


def count_installed_router(homes, min_distance):
    count = 1
    cur_home = homes[0]
    for i in range(1, len(homes)):
        if homes[i] - cur_home >= min_distance:
            count += 1
            cur_home = homes[i]
    return count


def solution(router_number, homes):
    homes = sorted(homes)

    start = 1  # 간격의 최솟값
    answer = end = homes[-1] - homes[0]  # 간격의 최댓값

    while start <= end:
        mid = (start + end) // 2
        count = count_installed_router(homes, mid)
        if count < router_number:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer


N, C = map(int, input().split())
homes = [int(input()) for _ in range(N)]

print(solution(C, homes))
