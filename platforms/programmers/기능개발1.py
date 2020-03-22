def solution(progresses, speeds):
    answer = []
    while progresses:
        done = []
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            if progresses[i] >= 100:
                done.append(i)
        # print(done)
        # print(progresses)
        # print(speeds)
        all_done = True
        for i in range(len(done)):
            if i != done[i]:
                all_done = False
        if all_done:
            leng = len(done)
            if leng != 0:
                answer.append(leng)
                # print("answer",answer)
                progresses = progresses[leng:]
                speeds = speeds[leng:]
    #print(answer)
    return answer