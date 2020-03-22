def findLongest(dates, supplies, currentDate):
    M = -1
    nextIdx = 0
    for i in range(len(dates)):
        if M < stock - (dates[i] - currentDate) + supplies[i]:
            nextIdx = i
            M = stock - (dates[i] - currentDate) + supplies[i]
    return ()

def solution(stock, dates, supplies, k):
    currentDate = 0
    i = 0
    while currentDate < k:
        start = i
        for idx in range(i, len(dates)):
            if dates[idx] <= currentDate + stock: # 공장은 (currentDate + stock)일 까지 라면을 생산할 수 있다.
                end = idx+1
        nextDate, nextSup = findLongest(dates[start:end],supplies[start:end],currentDate)

        # stock += supplies[i]
        # dateSum += x
    # return answer

[4, 9, 10, 19, 23, 25, 29]
[20,5, 5, 4, 5, 3, 10]
print(solution(4, [4, 10, 15], [20, 5, 10], 30))
