from collections import Counter

def solution(s):
    # s = sorted(s, reverse = True)    
    # print(s)
    # for i in range(len(s)):
    ans = 0
    s = Counter(s)
    print(s, ans)
    
    # (4)
    ans += s[4]
    del s[4]
    print(s, ans)

    # (3, 1)
    taxi = min(s[3], s[1])
    ans += taxi
    s[3] -= taxi
    s[1] -= taxi
    if s[3] <= 0:
        del s[3]
    if s[1] <= 0:
        del s[1]
    print(s, ans)

    # (2, 2)
    taxi = s[2] // 2
    ans += taxi
    s[2] -= taxi * 2
    if s[2] <= 0:
        del s[2]
    print(s, ans)
    
    # (2, 1, 1)
    if s[2] == 1:
        ans += 1
        del s[2]
        # (2, 1, 1)
        if s[1] >= 2:
            s[1] -= 2
        # (2, 1)
        elif s[1] == 1:
            s[1] -= 1
    if s[1] <= 0:
        del s[1]

    # (1, 1, 1, 1)
    ans += s[1] // 4
    if s[1] % 4 != 0:
        ans += 1
        

    # remainder
    for v in s.values():
        ans += v
    return ans
    
print(solution(	[1, 2, 4, 3, 3]))
print(solution(	[2, 3, 4, 4, 2, 1, 3, 1]))