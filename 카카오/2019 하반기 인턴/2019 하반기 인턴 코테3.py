import pprint
import itertools
import copy

def solution(user_id, banned_id):
    answer = 0
    dic = {}
    for b in banned_id:
        case = 0
        s = set()
        for u in user_id:
            size = len(b)
            found = True
            if size == len(u):
                for i in range(size):
                    if b[i] != '*' and b[i] != u[i]:
                        found = False
                        break
            else:
                found = False
            if found:
                s.add(u)
        # print(s)
        d = dic.get(b)
        if not d:
            dic[b] = [s, 1]
        else:
            dic[b][1] += 1
    # print()
    # print(dic)
    # print()
    temp = []
    for k, v in dic.items():
        if not temp:
            temp.extend([set(x) for x in itertools.combinations(v[0], v[1])])
            # print(temp)
        else:
            temp2 = []
            for t in itertools.combinations(v[0], v[1]):
                for tup in temp:
                    new = tup | set(t)
                    temp2.append(new)
            temp = copy.deepcopy(temp2)
    print("temp : ", temp)
    for s in temp:
        if len(s) == len(banned_id):
            answer += 1
    return answer

a = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*****", "******"])
print(a)
a = solution(["frodo", "frodi"], ["*****", "*****"])
print(a)
a = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
print(a)
a = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
print(a)