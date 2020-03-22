def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(w, h):
    if w > h:
        w, h = h, w
    mul = gcd(w, h)
    ww, hh = w // mul, h // mul
    cnt = hh + ww - 1
    return w * h - cnt * mul


print(solution(8, 12))
