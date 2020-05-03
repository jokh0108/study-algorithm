# not completed 86.4%


def convert_to_ms(h, m, s):
    return int((h*3600 + m * 60 + s)*1000)


def check(lines, answer, start, plus):
    for i in range(len(lines)):
        cnt = 0
        if start and plus:
            a, b = lines[i][0], lines[i][0] + 999
        elif start and not plus:
            a, b = lines[i][0] - 999, lines[i][0]
        elif not start and plus:
            a, b = lines[i][1], lines[i][1] + 999
        elif not start and not plus:
            a, b = lines[i][1] - 999, lines[i][1]

        for j in range(len(lines)):
            left, right = lines[j]
            if a <= left <= b:
                print(f'a: {a}, left: {left}, b: {b}')
                cnt += 1
            elif a <= right <= b:
                print(f'a: {a}, right: {right}, b: {b}')
                cnt += 1
        if answer < cnt:
            answer = cnt
    return answer


def solution(lines):
    answer = 0
    converted_lines = []
    for line in lines:
        _, S, T = line.split()
        h, m, s = map(float, S.split(":"))
        end = convert_to_ms(h, m, s)
        start = end - int(float(T[:-1]) * 1000) + 1
        if start < 0:
            start = 0
        print("start, end", start, end)
        converted_lines.append((start, end))
    converted_lines = sorted(converted_lines, key = lambda x: x[0])
    print(*converted_lines, sep='\n')
    answer = check(converted_lines, answer, True, True)
    answer = check(converted_lines, answer, True, False)
    answer = check(converted_lines, answer, False, True)
    answer = check(converted_lines, answer, False, False)
    return answer


print(solution(["2016-09-15 00:00:00.000 3s"]))
print(solution(["2016-09-15 23:59:59.999 0.001s"]))
print(solution([    "2016-09-15 01:00:04.001 2.0s",    "2016-09-15 01:00:07.000 2s"]))
print(solution([    "2016-09-15 01:00:04.002 2.0s",    "2016-09-15 01:00:07.000 2s"]))
print(solution([    "2016-09-15 20:59:57.421 0.351s",    "2016-09-15 20:59:58.233 1.181s",    "2016-09-15 20:59:58.299 0.8s",    "2016-09-15 20:59:58.688 1.041s",   "2016-09-15 20:59:59.591 1.412s",    "2016-09-15 21:00:00.464 1.466s",    "2016-09-15 21:00:00.741 1.581s",    "2016-09-15 21:00:00.748 2.31s",    "2016-09-15 21:00:00.966 0.381s",   "2016-09-15 21:00:02.066 2.62s"]))
