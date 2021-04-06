from typing import List


def can_compress(video_1d: str):
    return len(set(video_1d)) == 1


def make_quadtree(n: int, video: List[str]):
    if n == 0:
        return
    video_1d = "".join(video)
    if can_compress(video_1d):
        return video_1d[0]
    half = n // 2
    I = [row[:half] for row in video[:half]]
    II = [row[half:] for row in video[:half]]
    III = [row[:half] for row in video[half:]]
    IV = [row[half:] for row in video[half:]]
    return f"({make_quadtree(half, I)}{make_quadtree(half, II)}{make_quadtree(half, III)}{make_quadtree(half, IV)})"


def solution(n, video):
    return make_quadtree(n, video)


n = int(input())
video = [input() for _ in range(n)]

print(solution(n, video))
