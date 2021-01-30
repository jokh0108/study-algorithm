# timetable을 시간 순으로 오름차순 정렬
# 버스도 가능한 시간 순으로 timtable 형태로 저장
#       ex) [540, 600, 660, 720, 780, 840, 900, 960, 1020, 1080]
# con을 00:00 ~ 23:59 까지 모든 케이스를 timetable에 저장하면서 완전 탐색
#       ex)
#       [(479, 'con'), (480, 'x'), (549, 'x'), (550, 'x')]
#       [(480, 'x'), (480, 'con'), (549, 'x'), (550, 'x')]
# # 한 버스에 대해서 버스 출발 시간보다 이전의 대기열에 있는 크루들을 태움
#       이 중에 콘이 있으면, 최대 값 갱신
# 다음 버스로 이동하는 조건은 다음 두 개
# 1. 버스 출발 시간보다 늦게 대기한 크루가 있거나
# 2. 버스에 인원이 꽉찬 경우

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
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
# print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
# print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
# print(solution(1, 1, 1, ["23:59"]))
# print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))