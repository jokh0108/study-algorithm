def solution(arrangement):
    pieces = 0
    rods = 0
    stack = [arrangement[0]]
    for i in range(1, len(arrangement)):
        if arrangement[i] == '(':
            # push
            stack.append(arrangement[i])
            if arrangement[i-1] == '(':
                pieces +=1
                rods +=1
            else:
                pass
        else: # arrangement[i] == ')'
            # pop 
            temp = stack.pop()
            if arrangement[i-1] == '(':
                pieces += rods
            else:
                rods -= 1
    #print(pieces)
    return pieces

solution("()(((()())(())()))(())")