def solution(arrA, arrB):
    start= -1
    if len(arrA) != len(arrB):
        return False
    length = len(arrA)
    for i in range(length):
        if arrA[0] == arrB[i]:
            ## 중복일 경우는?
            for j in range(1, length):
                start = (start + 1)%length
                if arrA[j] != arrB[start]:
                    break
                last = j
            if arrA[last] == arrB[start]:
                return True
            ## slicing 한다면?
    return False
