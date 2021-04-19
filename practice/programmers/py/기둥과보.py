PILLAR = 0
BEAM = 1

DELETE = 0
INSTALL = 1


def solution(n, build_frame):
    def is_pillar_able(col: int, row: int, build) -> bool:
        if row == 0:
            return True
        if col > 0 and build[row][col - 1][BEAM]:
            return True
        if build[row][col][BEAM]:
            return True
        if row > 0 and build[row - 1][col][PILLAR]:
            return True
        return False

    def is_beam_able(col: int, row: int, build) -> bool:
        if row > 0 and build[row - 1][col][PILLAR]:
            return True
        if row > 0 and col < n and build[row - 1][col + 1][PILLAR]:
            return True
        if (
            col > 0
            and col < n
            and build[row][col - 1][BEAM]
            and build[row][col + 1][BEAM]
        ):
            return True
        return False

    answer = []
    build = [[[False, False] for _ in range(n + 1)] for _ in range(n + 1)]
    for col, row, structure, action in build_frame:
        print(*build, sep="\n")
        print(col, row, structure, action)
        if (
            action == INSTALL
            and structure == PILLAR
            and is_pillar_able(col, row, build)
        ):
            build[row][col][PILLAR] = True
        if action == INSTALL and structure == BEAM and is_beam_able(col, row, build):
            build[row][col][BEAM] = True

        if action == DELETE:
            build[row][col][structure] = False
            if structure == PILLAR:
                if (
                    not is_pillar_able(col, row + 1, build)
                    or not is_beam_able(col - 1, row + 1, build)
                    or not is_beam_able(col, row + 1, build)
                ):
                    build[row][col][structure] = True
                    continue
            if structure == BEAM:
                if (
                    (
                        build[row][col + 1][PILLAR]
                        and not is_pillar_able(col + 1, row, build)
                    )
                    or (build[row][col][PILLAR] and not is_pillar_able(col, row, build))
                    or (
                        build[row][col - 1][BEAM]
                        and not is_beam_able(col - 1, row, build)
                    )
                    or (
                        build[row][col + 1][BEAM]
                        and not is_beam_able(col + 1, row, build)
                    )
                ):
                    build[row][col][structure] = True
    print(*build, sep="\n")
    for col in range(n + 1):
        for row in range(n + 1):
            if build[row][col][PILLAR]:
                answer.append([col, row, PILLAR])
            if build[row][col][BEAM]:
                answer.append([col, row, BEAM])
    return answer


# print(
#     solution(
#         5,
#         [
#             [1, 0, 0, 1],
#             [1, 1, 1, 1],
#             [2, 1, 0, 1],
#             [2, 2, 1, 1],
#             [5, 0, 0, 1],
#             [5, 1, 0, 1],
#             [4, 2, 1, 1],
#             [3, 2, 1, 1],
#         ],
#     )
# )
print()
print(
    solution(
        5,
        [
            [0, 0, 0, 1],
            [2, 0, 0, 1],
            [4, 0, 0, 1],
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [2, 1, 1, 1],
            [3, 1, 1, 1],
            [2, 0, 0, 0],
            [1, 1, 1, 0],
            [2, 2, 0, 1],
        ],
    )
)
