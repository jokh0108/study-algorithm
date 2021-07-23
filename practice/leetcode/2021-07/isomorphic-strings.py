def isIsomorphic(s: str, t: str):
    d1, d2 = {}, {}
    for c1, c2 in zip(s, t):
        if (c1 not in d1) and (c2 not in d2):
            d1[c1] = c2
            d2[c2] = c1
            continue
        if d1.get(c1) != c2 or d2.get(c2) != c1:
            return False
    return True


print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("paper", "title"))
print(isIsomorphic("badc", "baba"))
