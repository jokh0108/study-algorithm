
import collections


def solution(paragraph, banned):
    paragraph = "".join(
        [char.lower() for char in paragraph if char.isalpha() or char == ' '])
    print(paragraph)
    counter = collections.Counter(paragraph.split())
    for banned_word in banned:
        del counter[banned_word]
    print(counter)
    return counter.most_common()[0][0]


print(solution("Bob hit a ball, the hit BALL flew far after it was hit.",
               ["hit"]))
