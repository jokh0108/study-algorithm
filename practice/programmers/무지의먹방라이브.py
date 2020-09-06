from collections import deque

def solution(food_times, k):
    if len(food_times) >= k:
        return k % len(food_times) + 1
    food_times = deque(sorted([[i, v] for i, v in enumerate(food_times)], key=lambda x: x[1]))
    print(food_times)
    rotation_stack = 0
    while food_times:
        print('rotation_stack',rotation_stack)
        n = len(food_times)
        next_rotation = food_times[0][1] - rotation_stack
        rotation_stack += next_rotation
        print(food_times, k, 'next_rotation',next_rotation, 'remain', k - next_rotation * n)
        if k - next_rotation * n >= 0:
            food_times.popleft()
            while food_times and food_times[0][1] == next_rotation:
                food_times.popleft()
            k = k - next_rotation * n
        else:
            break
    if not food_times:
        return -1
    print(food_times, k)
    print('-'*20)
    food_times = sorted(food_times, key=lambda x: x[0])
    print(food_times)
    idx = k % len(food_times)
    return food_times[idx][0] + 1


print(solution([5, 5, 5], 15))
# print(solution([3, 2, 3, 3, 3, 3, 3], 1))
# print(solution([3, 2, 3, 3, 3, 3, 3], 2))
# print(solution([3, 2], 2))
# print(solution([3, 2], 3))
# print(solution([3, 2], 4))
# print(solution([3, 2], 5))
# print(solution([3, 2], 6))
# print(solution([3, 2], 7))
# print(solution([50], 47))
# print(solution([50], 48))
# print(solution([50], 49))
# print(solution([50], 50))
# print(solution([50], 51))
# print(solution([50], 52))
# print(solution([50], 53))
# print(solution([50], 54))
# print(solution([50], 55))