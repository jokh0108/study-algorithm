# 86.4%

def convert_to_ms(h, m, s):
    return int((h*3600 + m * 60 + s)*1000)

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
    print('start')
    for i in range(len(converted_lines)):
        cnt = 0
        start, start_plus_1sec = converted_lines[i][0], converted_lines[i][0] + 999
        for j in range(len(converted_lines)):
            left, right = converted_lines[j]
            if start <= left <= start_plus_1sec:
                print(f'{start}, left: {left}, {start_plus_1sec}')
                cnt += 1
            elif start <= right <= start_plus_1sec:
                print(f'{start}, right: {right}, {start_plus_1sec}')
                cnt += 1
        if answer < cnt:
            answer = cnt       
    print('end') 
    converted_lines = sorted(converted_lines, key = lambda x: x[1])
    for i in range(len(converted_lines)):
        cnt = 0
        end, end_plus_1sec = converted_lines[i][1], converted_lines[i][1] + 999
        for j in range(len(converted_lines)):
            left, right = converted_lines[j]
            if end <= left <= end_plus_1sec:
                print(f'{end}, left: {left}, {end_plus_1sec}')
                cnt += 1
            elif end <= right <= end_plus_1sec:
                print(f'{end}, right: {right}, {end_plus_1sec}')
                cnt += 1
        if answer < cnt:
            answer = cnt            
    return answer


print(solution(["2016-09-15 00:00:00.000 3s"]))
print(solution(["2016-09-15 23:59:59.999 0.001s"]))
print(solution([    "2016-09-15 01:00:04.001 2.0s",    "2016-09-15 01:00:07.000 2s"]))
print(solution([    "2016-09-15 01:00:04.002 2.0s",    "2016-09-15 01:00:07.000 2s"]))
print(solution([    "2016-09-15 20:59:57.421 0.351s",    "2016-09-15 20:59:58.233 1.181s",    "2016-09-15 20:59:58.299 0.8s",    "2016-09-15 20:59:58.688 1.041s",   "2016-09-15 20:59:59.591 1.412s",    "2016-09-15 21:00:00.464 1.466s",    "2016-09-15 21:00:00.741 1.581s",    "2016-09-15 21:00:00.748 2.31s",    "2016-09-15 21:00:00.966 0.381s",   "2016-09-15 21:00:02.066 2.62s"]))
