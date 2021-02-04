#!/bin/python3

import math
import os
import random
import re
import sys


from collections import Counter

def make_palindrome(string):
    counter = Counter()
    for c in string:
        counter[c] += 1
    # print(string, counter)

    odd_count = 0
    odd_char = ""
    for char, count in counter.items():
        if count % 2 == 1:
            odd_count += 1
            odd_char = char

    if odd_count > 1 or (odd_count == 1 and len(string) % 2 == 0):
        return "no"

    front, back = "", ""
    for char, count in counter.items():
        add_on = char * (count // 2)
        front = front + add_on
        back = add_on + back

    if odd_count == 1:
        return front + odd_char + back
    return front + back


def scatterPalindrome(strToEvaluate):
    answer = []
    for string in strToEvaluate:
        cache = {}
        cnt = 0
        for i in range(len(string)):
            for j in range(i+1, len(string)+1):
                if string[i:j] in cache:
                    cnt += 1
                    continue
                palindrome = make_palindrome(string[i:j])
                if palindrome != "no":
                    cnt += 1
                    cache[string[i:j]] = palindrome
        answer.append(cnt)
    return answer
if __name__ == '__main__':



# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys



# from collections import Counter

# def make_palindrome(string):
#     counter = Counter()
#     for c in string:
#         counter[c] += 1
#     # print(string, counter)

#     odd_count = 0
#     odd_char = ""
#     for char, count in counter.items():
#         if count % 2 == 1:
#             odd_count += 1
#             odd_char = char

#     if odd_count > 1 or (odd_count == 1 and len(string) % 2 == 0):
#         return "no"

#     front, back = "", ""
#     for char, count in counter.items():
#         add_on = char * (count // 2)
#         front = front + add_on
#         back = add_on + back

#     if odd_count == 1:
#         return front + odd_char + back
#     return front + back


# def scatterPalindrome(strToEvaluate):
#     answer = []
#     for string in strToEvaluate:
#         cnt = 0
#         for i in range(len(string)):
#             for j in range(i+1, len(string)+1):
#                 palindrome = make_palindrome(string[i:j])
#                 if palindrome != "no":
#                     cnt += 1
#         answer.append(cnt)
#     return answer

# if __name__ == '__main__':
