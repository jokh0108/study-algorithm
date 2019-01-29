def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = [bridge_length]*len(truck_weights)
    w_index = 0 # # of the truck waiting to cross
    while time[-1] != 0:
        w =0 
        #print(w_index)
        for i in range(w_index):
            # if   time[i] == 0 -> crossed
            # else time[i] != 0 -> crossing
            if time[i] > 0:
                w += truck_weights[i]
        if w_index != len(truck_weights):
            if w + truck_weights[w_index] <= weight:
                w_index += 1
        for i in range(w_index):
            # if   time[i] == 0 -> crossed
            # else time[i] != 0 -> crossing
            if time[i] > 0:
                time[i] -= 1
        answer +=1 
    answer +=1
    #print(answer)
    return answer

solution(2,10,[7,4,5,6])
solution(100,100,[10])
solution(100,100,[10]*10)
