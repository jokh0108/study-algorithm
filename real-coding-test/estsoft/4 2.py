import collections

def solution(S, C):
    S = S.split('; ')
    s = [x.lower() for x in S]
    ss = [x.split() for x in s]
    c = C.lower()
    d = collections.defaultdict(int)
    email_name = ["_".join(["".join(x[-1].split('-')), x[0]]) for x in ss]
    counter = collections.Counter(email_name)
    for i in range(len(email_name)-1, -1, -1):
        full = email_name[i]
        if counter[email_name[i]] > 1:
            full += str(counter[email_name[i]])
            counter[email_name[i]] -= 1
        email_name[i] = S[i] + " <" + full + "@" + c + ".com>"
    return "; ".join(email_name)

print(solution('John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker', 'Example'))