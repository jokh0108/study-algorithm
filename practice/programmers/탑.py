def solution(heights):
    answer = []
    for i in range(len(heights)-1,0,-1):
        receiver =-1
        for j in range(i-1,-1,-1):
            if heights[j] > heights[i]:
                receiver = j
                break
        answer.insert(0, receiver+1)
    answer.insert(0, 0)

    print(answer, len(answer))
    return answer

solution([6, 9, 5, 7, 4])
solution([103, 9, 9, 3, 5, 7, 2])
solution([1, 5, 3, 6, 7, 6, 5])
solution([100,1])
#solution([100]*100)