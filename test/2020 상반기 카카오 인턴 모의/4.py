# binary search? heap?

def solution(k, room_number):
    answer = []
    s = set([0])
    for n in room_number:
        if n not in s:
            answer.append(n)
            s.add(n)
        else:
            ss = set(range(n, max(s)+2)) - s
            print(ss)
            target = min(ss)
            answer.append(target)
            s.add(target)
    return answer

print(solution(10, [1, 3, 4, 1, 3, 1]))