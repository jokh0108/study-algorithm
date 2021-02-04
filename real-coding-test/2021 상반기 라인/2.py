import collections


def solution(ball, order):
    ball_queue = collections.deque(ball)
    print(ball_queue)
    ready_set = set()
    answer = []
    for ball_to_pop in order:            
        if ball_to_pop == ball_queue[0]:
            answer.append(ball_queue.popleft())
            while ball_queue and ball_queue[0] in ready_set:
                ready_set.remove(ball_queue[0])
                answer.append(ball_queue.popleft())
        elif ball_to_pop == ball_queue[-1]:
            answer.append(ball_queue.pop())
            while ball_queue and ball_queue[-1] in ready_set:
                ready_set.remove(ball_queue[-1])
                answer.append(ball_queue.pop())
        else:
            ready_set.add(ball_to_pop)
        # print(answer, ready_set)

    return answer



print(solution([1, 2, 3, 4, 5, 6], [6, 2, 5, 1, 4, 3]))
print(solution([11, 2, 9, 13, 24], [9, 2, 13, 24, 11]))
