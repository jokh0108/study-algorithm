def solution(progresses, speeds):
    answer = []
    while progresses:
        last = len(progresses) + 100
        canRelease = False
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            if progresses[i] >= 100:
                if i == 0:
                    canRelease = True
                    last = i
                else:
                    if canRelease:
                        last = i
            else:
                canRelease = False
        if last < len(progresses):
            answer.append(last+1)
            progresses = progresses[last+1:]
            speeds = speeds[last+1:]
                
        # if progresses[0] >= 100:
        #     last = 0
        #     for i in range(1, len(progresses)):
        #         if progresses[i] >= 100:
        #             last = i
        #         else:
        #             break
    
        
   # print(answer)
    return answer 

solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5 , 10, 7])
solution( [93, 30, 55, 60, 40, 65], [1, 30, 5 , 10, 60, 7])