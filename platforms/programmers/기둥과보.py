import collections


def solution(n, build_frame):
    answer = []
    build = collections.defaultdict(int)
    print(*build_frame, sep='\n')
    for x, y, a, b in build_frame:
        if b == 1:
            if a == 0:
                if y == 0 or \
                    (x >= 1 and build.get((x-1, y)) == 1) or \
                        (y >= 1 and build.get((x, y-1)) == 0):
                    build[(x, y)] = a
            else:
                if y >= 1 and \
                        x+1 <= n and \
                        (
                            (build.get((x, y-1)) == 0 or
                             build.get((x+1, y-1)) == 0
                             ) or
                            (x-1 >= 0 and
                                (build.get((x-1, y)) == 1 and
                                 build.get((x+1, y)) == 1))
                        ):
                    build[(x, y)] = a
        else:
            if a == 0:
                pass
            else:
                pass
    print(build)
    for (x, y), a in build.items():
        answer.append([x, y, a])
    answer = sorted(answer, key=lambda x: (x[0], x[1], x[2]))
    return answer


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
      2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print()
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
      1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
