def solution(s1, s2, s3):
    i, j, k = 0, 0, 0
    while i < len(s1) and j < len(s2):
        print(s1[i], s2[j], s3[k])
        if s3[k] != s1[i] and s3[k] != s2[j]:
            return False
        if s3[k] == s1[i]:
            i += 1
            k += 1
            continue
        if s3[k] == s2[j]:
            j += 1
            k += 1
            continue

    if len(s1) + len(s2) != len(s3):
        return False
    return True


print(solution("aabcc", "dbbca", "aadbbcbcac"))
print(solution("aabcc", "dbbca", "aadbbbaccc"))
print(solution("a", "", "c"))
