min_count = 100
answer_num = 0

def solution(n):
    global min_count, answer_num
    min_count = 100
    answer_num = 0
    answer = []
    count = 0

    def solve(n, count):
        global min_count, answer_num
        n = str(n)
        if len(n) == 1:
            print(' ' * count,  n)
            min_count = min(min_count, count)
            answer_num = int(n)
        for i in range(1, len(n)):
            left, right = n[:i], n[i:]
            if right[0] == '0' and right[-1] != '0':
                continue
            print(' ' * count, left, right)
            solve(int(left) + int(right), count + 1)
                
    solve(n, count)

    return [min_count, answer_num]


print(solution(73425))
print(solution(10007))
print(solution(9))
