def solution(progresses, speeds):
    answer = []
    while progresses:
        done = []
        canRelease = False
        last = 0
        for i in range(len(progresses)-1, -1, -1):
            progresses[i] += speeds[i]
            if progresses[i] >= 100 :
                if canRelease == False:
                    last = i
                    canRelease = True
            else:
                canRelease = False
      #  print(progresses)
        if canRelease:
            answer.append(last + 1)
            progresses = progresses[last+1:]
            speeds = speeds[last+1:]
        
    print(answer)
    return answer 

solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5 , 10, 7])
solution( [93, 30, 55, 60, 40, 65], [1, 30, 5 , 10, 60, 7])