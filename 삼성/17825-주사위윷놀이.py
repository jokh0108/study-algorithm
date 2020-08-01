from collections import deque
line0 = list(range(0, 42, 2))
line1 = [0, 2, 4, 6, 8, 10, 13, 16, 19, 25, 30, 35, 40]
line2 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 25, 30, 35, 40]
line3 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 28, 27, 26, 25, 30, 35, 40]
horse = [(line0, 0), (line0, 0), (line0, 0), (line0, 0)]
print(
    line0,
    line1,
    line2,
    line3,
    sep='\n'
)
print(sum([2, 10, 4, 10, ]))
inputs = map(int, input().split())
inputs = [1, 2, 3]
lv = 0

def dfs(horse, score, step):
    