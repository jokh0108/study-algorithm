from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            return word == word[::-1]
        pairs = set()
        for i, a in enumerate(words):
            for j, b in enumerate(words):
                if i == j:
                    continue
                if is_palindrome(a+b):
                    pairs.add((i, j))
        return [list(pair) for pair in pairs]


solution = Solution()
print(solution.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
