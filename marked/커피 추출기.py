import collections
import heapq


def solution(N, coffee_times):
    coffee_times = [(time, i + 1) for i, time in enumerate(coffee_times[:])]
    pq = coffee_times[:N]
    coffee_times = collections.deque(coffee_times[N:])
    # (커피 추출이 끝날 시간(= 추출기에 투입된 시각 + 추출 시간), 주문 번호)
    heapq.heapify(pq)
    print(pq, coffee_times)
    answer = []
    while pq:
        complete_time, order_number = heapq.heappop(pq)
        answer.append(order_number)
        if coffee_times:
            next_time, next_order_number = coffee_times.popleft()
            heapq.heappush(pq, (next_time + complete_time, next_order_number))
        print(
            f"complete_time: {complete_time} second, order_number: #{order_number}",
            answer,
        )
    return answer


print(solution(3, [4, 2, 2, 5, 3]))
print(solution(1, [100, 1, 50, 1, 1]))
