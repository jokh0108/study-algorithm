minimum = 10
d = {}


# recurse 안에서 시계 / 반시계

def recurse(weak, dist, cnt, n, clockwise):
    global minimum
    global d
    print(56, weak, dist, cnt)
    if not weak:
        if minimum > cnt:
            minimum = cnt
        return
    elif len(weak) == 1:
        if minimum > cnt+1:
            minimum = cnt +1
        return
    else:
        key = tuple(sorted(list(weak)))
        if d.get(key):
            if len(d[key]) >= len(dist):
                return
            else:
                d[key] = dist
        else:
            d[key] = dist

    if dist:
        friend = dist.pop()
    else:
        return
    for w in weak:
        todo = weak.copy()
        #clock
        print(12, "friend", friend)
        steps = range(w, w+friend+1) if clockwise else range(w , w-friend-1, -1)
        for k in steps:
            k = k % n
            print(k, end=' ')
            if k in todo:
                todo.remove(k)
        print()
        if todo == weak: # 더 이상 답이 없음 => 지우려고 해봐도 안지워짐
            return
        else:
            recurse(todo, dist[:], cnt + 1, n, clockwise)

        #counter


def solution(n, weak, dist):
    global minimum
    global d
    minimum = 10
    d = {}
    dist = sorted(dist)
    recurse(set(weak), dist[:], 0, n, True)
    print(d)
    d = {}
    recurse(set(weak), dist[:], 0, n, False)
    print(d)
    return minimum


print("answer", solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print("answer", solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
