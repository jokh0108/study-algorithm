import pprint

def solution(s):
    answer = []

    ts = s[2:-2].split("},{")
    ts = sorted(ts, key=lambda x: len(x))
    # print(ts)
    prev = set()
    for i in range(len(ts)):
        tuple_set = set(map(int, ts[i].split(",")))
        # print(tuple_set, prev)
        answer.append((tuple_set - prev).pop())
        prev = tuple_set
    return answer

a = solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
print(a)
a = solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
print(a)
a = solution("{{20,111},{111}}")
print(a)
a = solution("{{123}}"	)
print(a)
a = solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"	)
print(a)
