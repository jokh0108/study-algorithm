# 암호 만들기

from itertools import combinations

MIN_VOWEL_NUMBER = 1
MIN_CONSONANATS_NUMBER = 2


def solution(L, chars):
    passwords = []
    for combination in combinations(chars, L):
        vowels = [char for char in combination if char in {"a", "e", "i", "o", "u"}]
        consonants = [
            char for char in combination if char not in {"a", "e", "i", "o", "u"}
        ]
        if len(vowels) < MIN_VOWEL_NUMBER:
            continue
        if len(consonants) < MIN_CONSONANATS_NUMBER:
            continue
        passwords.append("".join(sorted(vowels + consonants)))
    return sorted(passwords)


L, _ = map(int, (input().split()))
chars = input().split()

for answer in solution(L, chars):
    print(answer)
