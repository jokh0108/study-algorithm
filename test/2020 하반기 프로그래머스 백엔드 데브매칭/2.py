from datetime import datetime, timedelta

def solution(p,n):
    before_time = datetime.strptime(p, '%p %I:%M:%S')
    after_time = before_time + timedelta(seconds=n)
    return after_time.strftime("%H:%M:%S")
print(solution("PM 01:00:00", 10))
print(solution("PM 11:59:59", 1))