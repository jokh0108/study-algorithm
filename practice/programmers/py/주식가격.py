def solution(prices):
    leng = len(prices)
    answer = [1]*(leng - 1)+[0]
    #print(answer)
    for i in range(leng-1, 0, -1):
        if prices[i-1] <= prices[i]:
            answer[i-1] += answer[i]
        print(answer)
        print(prices)
        print()

    print(answer)

    return answer
solution([1,2, 3, 4, 5, 6, 7, 6, 5, 4,3])
solution([1, 2,3, 5, 6, 10000, 9999, 4053, 2222, 5, 4, 3, 6, 7])