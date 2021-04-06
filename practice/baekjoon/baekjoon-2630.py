def all_blue(matrix):
    return all([all([unit == 1 for unit in row]) for row in matrix])


def all_white(matrix):
    return all([all([unit == 0 for unit in row]) for row in matrix])


def cut(paper, m, is_white):
    if m == 0:
        return 0
    if is_white and all_white(paper):
        return 1
    if not is_white and all_blue(paper):
        return 1

    half = m // 2
    I = [row[:half] for row in paper[:half]]
    II = [row[half:] for row in paper[:half]]
    III = [row[:half] for row in paper[half:]]
    IV = [row[half:] for row in paper[half:]]

    return (
        cut(I, half, is_white)
        + cut(II, half, is_white)
        + cut(III, half, is_white)
        + cut(IV, half, is_white)
    )


def solution(m, paper):
    white = cut(paper, m, is_white=True)
    blue = cut(paper, m, is_white=False)
    return white, blue


n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

print(*solution(n, paper), sep="\n")
