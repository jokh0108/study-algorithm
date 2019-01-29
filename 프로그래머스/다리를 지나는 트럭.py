def isTruckInBridge(bridge):
    for b in bridge:
        #print(bridge)
        if b != []:
            return True
    return False

def bridgeSum(bridge):
    s = 0
    for b in bridge:
        s += sum(b)
    return s

def solution(bridge_length, weight, truck_weights):
    answer = 0
    crossed = []
    bridge = []
    for i in range(bridge_length):
        bridge.append(crossed[:])
    #print(crossed, bridge, truck_weights)
    
    while isTruckInBridge(bridge) or truck_weights:
        #break
        if bridge[0]:
            crossed.append(bridge[0].pop(0))
        for i in range(1, len(bridge)):
            if bridge[i]:
                bridge[i-1].append(bridge[i].pop(0))
        if truck_weights :
            w1 = bridgeSum(bridge)
            w2 = truck_weights[0]            
            if w1 + w2 <= weight:
                bridge[-1].append(truck_weights.pop(0))
        answer +=1 
        #print(crossed, bridge, truck_weights)
    #print(answer)
    return answer

solution(2,10,[7,4,5,6])
solution(100,100,[10])
solution(100,100,[10]*10)
