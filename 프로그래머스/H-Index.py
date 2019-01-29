def solution(citations):
    citations = sorted(citations)
    H_Index = 0
    i=0
    length = len(citations)
    for h in range(citations[-1]+1):
        if length - i >= h:
            H_Index = h
        if h == citations[i]:
            while i < length and h == citations[i] :
                i+=1
         
    print(H_Index)
    return H_Index
    ## 중복 생각하기!!!!

solution([1, 2, 3, 3, 3, 3, 4, 4, 5, 6, 
7, 7, 8, 8, 9, 9, 10, 10, 10])