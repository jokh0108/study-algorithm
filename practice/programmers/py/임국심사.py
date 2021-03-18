def solution(n, times):
    start = 0
    answer = end = 10**9 * 10**9
    while start <= end:
        mid = (start + end) // 2
        # mid까지 곱하면 모든 심사원이 심사를 했다는 뜻이 된다.
        # 실제로는 일부만 심사를 한다. (testcase: 4, [1, 1, 1])
        # 그러므로 mid - 1까지 곱하고 mid에 딱 심사가 끝날만한 심사원의 케이스만 추가해준다.
        immigrants = sum([(mid - 1) // time for time in times])
        for time in times:
            if mid % time == 0:
                immigrants += 1
                if immigrants == n:
                    break
        print("immigrants", immigrants, "start", start,
              "mid", mid, "end", end, "answer", answer)
        if immigrants == n:
            end = mid - 1
            answer = min(answer, mid)
        elif immigrants < n:
            start = mid + 1
        else:
            end = mid - 1
    return answer


print(solution(6, [7, 10]))
# print(solution(4, [1, 1, 1]))
