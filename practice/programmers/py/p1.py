def solution(v):
    x_dict ={}
    y_dict = {}
    answer = []
    for each in v:
        if x_dict.get(each[0])==None:
            x_dict[each[0]] = 1
        else:
            x_dict[each[0]] += 1
        
        if y_dict.get(each[1])==None:
            y_dict[each[1]] = 1
        else:
            y_dict[each[1]] += 1
    print(x_dict, y_dict)
    for i in x_dict.items():
        if i[1] == 1:
            answer.append(i[0])
    for i in y_dict.items():
        if i[1] == 1:
            answer.append(i[0])
    print(answer)
    #return answer
solution([[1, 4], [3, 4], [3, 10]])