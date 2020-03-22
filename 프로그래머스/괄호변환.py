def is_correct(u):
    st = []
    for x in u:
        if x == '(':
            st.append(x)
        else:
            if not st:
                return False
            st.pop()
    if st:
        return False
    return True

def split(w):
    left, right = 0, 0
    pos = -1
    for i in range(len(w)):
        if w[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u, v = w[:i+1], w[i+1:]
            break
    print(u, v)
    return u, v

def convert(w):
    if not w:
        return w
    u, v = split(w)
    if is_correct(u):
        u += convert(v)
        return u
    else:
        new = '('


def solution(p):
    answer = convert(p)
    return answer