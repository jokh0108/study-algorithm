def isRun(t):
    size = len(t)
    for i in range(size - 2):
        if t[i] > 0 and t[i+1] > 0 and t[i+2] > 0:
            # print(t[i:i+2])
            return True
    return False

def isTriplet(t):
    if t >= 3:
        return True
    return False

T = int(input())
for i in range(T):
    cards = list(map(int, input().split()))
    p1 = [0]*10
    p2 = [0]*10
    # print(p1)
    # print(p2)
    winner = 0
    # print(cards)
    for j in range(0, len(cards), 2):
        # print(cards[j:j+2])
        c1, c2 = cards[j:j+2]

        p1[c1] += 1
        # print(p1)
        start, end = c1-2, c1+2
        if start < 0:
            start = 0
        if end > 9:
            end = 9
        if isRun(p1[start:end+1]) or isTriplet(p1[c1]):
            winner = 1
            break

        p2[c2] += 1
        # print(p2)
        start, end = c2-2, c2+2
        if start < 0:
            start = 0
        if end > 9:
            end = 9
        if isRun(p2[start:end+1]) or isTriplet(p2[c2]):
            winner = 2
            break

    print("#%d" % (i+1), winner)
