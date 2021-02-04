opening = ['(', '{', '[', '<']
closing = [')', '}', ']', '>']

def solution(inputString):
    st = []
    answer = 0
    for c in inputString:
        if c in opening:
            st.append(c)
        elif c in closing:
            if not st:
                return -1
            else:
                st.pop()
                answer += 1
    return answer