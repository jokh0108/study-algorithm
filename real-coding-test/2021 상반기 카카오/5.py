def convert_to_second(time):
    HH, MM, SS = map(int, time.split(':'))
    return HH * 3600 + MM * 60 + SS


def convert_to_time(second):
    HH = second // 3600
    second = second % 3600
    MM = second // 60
    SS = second % 60
    return f'{HH:02d}:{MM:02d}:{SS:02d}'


def solution(play_time, adv_time, logs):
    TIME_MAX = 99*60*60 + 60 * 59 + 60
    time_line = [0] * TIME_MAX
    play_time_delta = convert_to_second(play_time)
    adv_time_delta = convert_to_second(adv_time)
    for log in logs:
        start, end = map(convert_to_second, log.split('-'))
        for time in range(start, end+1):
            time_line[time] += 1

    adv_time_window_start = 0
    prev_accumulated_time = sum(time_line[:adv_time_delta])
    max_time = prev_accumulated_time
    default_time = 0

    while adv_time_window_start + adv_time_delta < play_time_delta:
        # print(adv_time_window_start + adv_time_delta, )
        curr_accumulated_time = prev_accumulated_time + \
            time_line[adv_time_window_start + adv_time_delta + 1] - \
            time_line[adv_time_window_start]
        if max_time < curr_accumulated_time:
            default_time = adv_time_window_start + 1
            max_time = curr_accumulated_time
            # print(max_time)
        prev_accumulated_time = curr_accumulated_time
        adv_time_window_start += 1
    return convert_to_time(default_time)


print(solution("02:03:55", "00:14:15", [
      "01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]))
print(solution("99:59:59", "25:00:00", [
      "69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", [
      "15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
