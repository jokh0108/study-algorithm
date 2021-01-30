dic = {"L": (-1, 0),
       "R": (+1, 0),
       "U": (0, +1),
       "D": (0, -1)}
from collections import defaultdict
from pprint import pprint

def solution(dirs):
    path = defaultdict(int)
    cur_pos = [0,0]
    for d in dirs:
        org_pos = cur_pos[:]
        prev_pos = cur_pos[:]
        next_pos = cur_pos[:]

        next_pos[0] += dic[d][0]
        next_pos[1] += dic[d][1]
        if next_pos[0] > 5 or next_pos[0] < -5 or next_pos[1] > 5 or next_pos[1] <-5:
            continue

        cur_pos = next_pos[:]
        prev_pos.extend(next_pos)
        next_pos.extend(org_pos)

        path[tuple(prev_pos)] = 1
        path[tuple(next_pos)] = 1
        # pprint(path, width=20)
    return sum(path.values())//2


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
