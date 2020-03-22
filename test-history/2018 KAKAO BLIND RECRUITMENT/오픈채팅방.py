def solution(records):
    answer = []
    user_nick = {}
    for record in records:
        record = record.split()
        action, uid = record[:2]
        if len(record) ==3:
            user_nick[uid] = record[2]     
        if action == 'Enter' or action == 'Leave':
            answer.append({"action" : action,"uid":uid })
        else:
            user_nick[uid] = record[2]    

        # print(answer, user_nick)
    for i in range(len(answer)):
        if answer[i]['action'] == 'Enter':
            answer[i] = user_nick[answer[i]["uid"]] + "님이 들어왔습니다."
        elif answer[i]['action'] == 'Leave':
            answer[i] = user_nick[answer[i]["uid"]] + "님이 나갔습니다."
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))