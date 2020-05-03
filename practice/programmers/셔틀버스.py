
def to_minute(HHMM):
    h, m = HHMM.split(':')
    return int(h) * 60 + int(m)

def to_HHMM(minute):
    HH, MM = minute // 60, minute % 60
    return f'{HH:02d}:{MM:02d}'

def solution(n, t, m, timetable):
    answer = 0
    converted_timetable = []
    for time in timetable:
        minute = to_minute(time)
        converted_timetable.append((minute, 'x'))
    converted_timetable = sorted(converted_timetable)

    bus_timetable = []
    bus_start = to_minute("09:00")
    for i in range(n):
        bus_timetable.append(bus_start + i * t)
    print(bus_timetable)

    idx = 0
    for con_time in range(24 * 60):
        con = (con_time, 'con')
        copied_tt = converted_timetable[:]
        while idx < len(copied_tt) and copied_tt[idx][0] <= con_time:
            idx += 1
        if idx == len(copied_tt):
            copied_tt.append(con)
        else:
            copied_tt.insert(idx, con)
        print(bus_timetable)
        print(copied_tt)

        bus_idx = 0
        tt_idx = 0
        boarded = 0
        con_boarded = False
        while bus_idx < len(bus_timetable):
            while tt_idx < len(copied_tt):
                print(bus_idx, tt_idx)
                time, name = copied_tt[tt_idx]
                if time <= bus_timetable[bus_idx]:
                    if name == 'con':
                        con_boarded = True
                    boarded += 1
                    tt_idx += 1
                    if boarded == m:
                        bus_idx += 1
                        boarded = 0
                        break
                else:
                    bus_idx += 1
                    boarded = 0
                    break
        if con_boarded:
            print('con boarded', con_time)
            answer = con_time
        else:
            return to_HHMM(answer)
    return to_HHMM(answer)

# print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
# print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
# print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
# print(solution(1, 1, 1, ["23:59"]))
# print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
