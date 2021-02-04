"""
interesting point
디지털로 표현된 시계 내 숫자가 최대 두개의 다른 숫자로만 표현되는 것
13:31:33 O
02:20:22 O
00:00:00 O
15:45:14 X

구간이 주어지면 interesting point가 몇 개 인가?

input으로는 S(start)와 T(end)가 주어진다.
예를 들어, 15:15:00 ~ 15:15:12(포함)면 15:15:11 1개
22:22:21 ~ 22:22:23 -> 3개

"""
def sec_to_clock(sec):
    HH = sec // 3600
    MM = (sec - HH * 3600) // 60
    SS = sec % 60
    return f'{HH:02}:{MM:02}:{SS:02}'

def clock_to_sec(clock):
    HH, MM, SS = map(int, clock.split(':'))
    return HH * 3600 + MM * 60 + SS

def is_interesting(clock):
    HH, MM, SS = clock.split(':')
    s = set(HH) | set(MM) | set(SS)
    return True if len(s) <= 2 else False

def solution(S, T):
    count = 0
    start = clock_to_sec(S)
    end = clock_to_sec(T)
    for time_in_sec in range(start, end + 1):
        clock = sec_to_clock(time_in_sec)
        print(time_in_sec, clock, clock_to_sec(clock))
        if is_interesting(clock):
            count += 1
    return count


print(solution("15:15:00", "15:15:12"))
print(solution("22:22:21", "22:22:23"))
