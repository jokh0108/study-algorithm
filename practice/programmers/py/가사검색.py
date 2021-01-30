import collections

class Node:
    def __init__(self, val, lv):
        self.val = val
        self.children = {}
        self.lv = lv
        self.tails = collections.defaultdict(set)

class Trie:
    def __init__(self):
        self.head = Node(None, 0)

    def insert(self, string, suffix_cnt, suffixes):
        curr_node = self.head
        for idx in range(len(string)):
            # print(curr_node.tails, curr_node.children)
            if (curr_node.lv, string[idx:]) in suffixes:
                suffix_cnt['?'*curr_node.lv+string[idx:]] += 1
            if len(string) - idx - 1 >= 1:
                # print(000, curr_node.val)
                curr_node.tails[len(string) - idx ].add(string[idx:])
            if string[idx] not in curr_node.children:
                curr_node.children[string[idx]] = Node(string[idx], idx+1)
            # print(988,curr_node.tails, curr_node.children, curr_node.lv)
            curr_node = curr_node.children[string[idx]]

    def starts_with(self, prefix, remained_len):
        curr_node = self.head
        subtrie = None
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return 0
        # print(5839, prefix, subtrie.tails)
        if remained_len in subtrie.tails:
            return len(subtrie.tails[remained_len])
        else:
            return 0


def split(string):
    for i in range(len(string)):
        if string[i] == '?':
            return i
    return -1

def split2(string):
    for i in range(len(string)):
        if string[i] != '?':
            return i
    return -1

def solution(words, queries):
    answer = []

    suffixes = set()
    for q in queries:
        if q[0] == '?' and q[-1] != '?':
            lv = split2(q)
            suffixes.add((lv, q[lv:]))
    # print(suffixes)

    t = Trie()
    suffix_cnt = collections.defaultdict(int)
    for word in words:
        t.insert(word, suffix_cnt, suffixes)
    # print(45345,suffix_cnt)

    # print(t.head.tails, t.head.children)
    for q in queries:
        if q[0] == '?' and q[-1] == '?':
            answer.append(t.head.tails[len(q)])
        elif q[-1] == '?':
            idx = split(q)
            prefix = q[:idx]
            answer.append(t.starts_with(prefix, len(q) - idx))
        elif q[0] == '?':
            answer.append(suffix_cnt[q])
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))