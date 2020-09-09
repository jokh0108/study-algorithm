def solution(msg):
    answer = []
    dic = {chr(ord('A') + i - 1): i for i in range(1, 27)}
    idx = 27
    i = 0
    
    w = msg[i]
    while True:
        if i+1 < len(msg):
            i += 1
            c = msg[i]
            if w + c in dic.keys():
                w = w + c
            else:
                answer.append(dic[w])
                dic[w+c] = idx
                idx += 1
                w = msg[i]
        else:
            answer.append(dic[w])
            break
    return answer
print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))
