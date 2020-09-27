def solution(blocks): 
    answer = [[blocks[0][1]]] 
    level = 1 
    while level < len(blocks): 
        k, num = blocks[level] 
        arr = [num]* (level + 1) 
        i = k -1
        while 0 <= i : 
            arr[i] = (answer[level-1][i] - arr[i+1]) 
            i -= 1

        i = k+1
        while i <= level: 
            arr[i] = (answer[level-1][i-1] - arr[i-1]) 
            i += 1

        print(arr) 
        answer.append(arr) 
        level += 1
    return [num for row in answer for num in row]

print(solution([[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]))
print(solution([[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]))