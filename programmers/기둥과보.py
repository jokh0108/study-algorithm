import collections


def is_pillar_able(x, y, build):
    # if y == 0 or (build.get((x - 1, y)) == 1) or (build.get((x, y - 1)) == 0):dngt
    #     return True
    if y == 0:
        print(1)
        return True
    elif build.get((x - 1, y)) == 1:
        print(2)
        return True
    elif build.get((x, y - 1)) == 0:
        print(3)
        return True
    return False


def is_beam_able(x, y, build):
#     if (build.get((x, y - 1)) == 0 or build.get((x + 1, y - 1)) == 0) or \
#             (build.get((x - 1, y)) == 1 and build.get((x + 1, y)) == 1):
#         return True
    if build.get((x, y - 1)) == 0:
        print(4)
        return True
    elif build.get((x + 1, y - 1)) == 0:
        print(5)
        return True
    elif build.get((x - 1, y)) == 1:
        print(6)
        if build.get((x + 1, y)) == 1:
            print(7)
            return True
    return False


def solution(n, build_frame):
    answer = []
    build = collections.defaultdict(int)
    # print(*build_frame, sep='\n')
    for x, y, a, b in build_frame:
        print(x, y, a, b)
        if b == 1:
            if a == 0:
                if is_pillar_able(x, y, build):
                    build[(x, y)] = a
            else:
                if is_beam_able(x, y, build):
                    build[(x, y)] = a
        else:
            if build.get((x, y), None) >= 0:
                del build[(x, y)]
                if a == 0:
                    if build.get((x, y + 1)) == 0 and not is_pillar_able(x, y + 1, build):
                        build[(x, y)] = a
                    if build.get((x - 1, y + 1)) == 1 and not is_beam_able(x - 1, y + 1, build):
                        build[(x, y)] = a
                    if build.get((x, y + 1)) == 1 and not is_beam_able(x, y + 1, build):
                        build[(x, y)] = a
                else:
                    if build.get((x + 1, y)) == 0 and not is_pillar_able(x + 1, y, build):
                        build[(x, y)] = a
                    if build.get((x - 1, y)) == 1 and not is_beam_able(x - 1, y, build):
                        build[(x, y)] = a
                    if build.get((x + 1, y)) == 1 and not is_beam_able(x + 1, y, build):
                        build[(x, y)] = a
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
print(solution(5, [[0, 0, 0, 1], [3, 0, 0, 1], [0, 1, 1, 1], [2, 1, 1, 1], [
    1, 1, 1, 1]]))
