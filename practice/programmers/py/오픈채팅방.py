import collections


def solution(records):
    result = []
    id_dict = collections.defaultdict(str)
    for record in records:
        temp = record.split()
        if len(temp) == 3:
            cmd, iid, nick = temp
        else:
            cmd, iid = temp
        if cmd == "Enter":
            id_dict[iid] = nick
            result.append((iid, "Enter"))
        elif cmd == "Leave":
            result.append((iid, "Leave"))
        else: # cmd == "Change"
            id_dict[iid] = nick

    # print(id_dict)
    enter = "들어왔습니다."
    leave = "나갔습니다."
    # print(result)
    result = [f'{id_dict[iid]}님이 ' + enter if action == "Enter" else f'{id_dict[iid]}님이 ' + leave for (iid, action) in result]
    return result


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234",
                "Enter uid1234 Prodo", "Change uid4567 Ryan"]))