# 정규표현식 ㄴ효율성 실패
# import re


# def solution(words, queries):
#     answer = []
#     for query in queries:
#         count = 0
#         pattern = "".join(["[\w]" if c == "?" else c for c in query])
#         for word in words:
#             matched = re.fullmatch(pattern, word)
#             if matched:
#                 count += 1
#         answer.append(count)
#     return answer


# prefix에 대한 Trie는 기본적인 개념이기 때문에 생각하기 쉬웠지만,
# suffix에 대한 Trie는 좀 생소해서 어떻게 해야할지 막막했다.

# suffix의 경우에는 parent를 매기는 방법 등을 생각해보았는데
# 더 생각해보니 reverse trie를 만드는 굉장히 획기적인 방법이 생각났다.
# 아마 예전에 어딘가서 본 적이 있었던 것 같다.

# reverse trie를 통해 굉장히 깔끔하면서도 쉬운 방식으로 정답을 추출할 수 있었다.
# 그런데도 불구하고 효율성 테스트 2개를 통과하지 못했다.
# 이 부분은 질문하기를 확인해서 길이별로 trie를 따로 두는 방식에 대한 힌트를 얻을 수 있었다.
# 덕분에 통과할 수 있었다.
# 여러가지 팁을 확인할 수 있었던 문제였다.

# Trie 기본 개념, Reversed Trie, 길이별 Trie 등 기억해두면 좋을 팁들을 알아낼 수 있었다.

import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node.count += 1
            node = node.children[char]

    def starts_with(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            node = node.children[char]
            print(char, node.count)
        return node.count


def solution(words, queries):
    answer = []
    trie_dict = {}
    reverse_trie_dict = {}
    for word in words:
        if len(word) in trie_dict:
            trie_dict[len(word)].insert(word)
        else:
            trie = Trie()
            trie.insert(word)
            trie_dict[len(word)] = trie

        if len(word) in reverse_trie_dict:
            reverse_trie_dict[len(word)].insert(word[::-1])
        else:
            trie = Trie()
            trie.insert(word[::-1])
            reverse_trie_dict[len(word)] = trie

    print(trie_dict, reverse_trie_dict)
    for query in queries:
        if query[0] != "?":
            index = query.find("?")
            prefix, tail = query[:index], query[index:]
            print(query)
            if len(query) in trie_dict:
                print(trie_dict[len(query)])
                count = trie_dict[len(query)].starts_with(prefix)
            else:
                count = 0
            answer.append(count)
            continue
        print(query)
        query = query[::-1]
        index = query.find("?")
        prefix, tail = query[:index], query[index:]
        if len(query) in reverse_trie_dict:
            print(reverse_trie_dict[len(query)])
            count = reverse_trie_dict[len(query)].starts_with(prefix)
        else:
            count = 0
        answer.append(count)

    return answer


print(
    solution(
        ["frodo", "front", "frost", "frozen", "frame", "kakao"],
        ["fro??", "????o", "fr???", "fro???", "pro?"],
    )
)
