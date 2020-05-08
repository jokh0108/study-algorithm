from pprint import pprint
def make_trie(words):
    root = {}
    for word in words:
        cur_dict = root
        for i in range(len(word)):
            if word[i] not in cur_dict:
                cur_dict[word[i]] = {'cnt': 1}
            else:
                cur_dict[word[i]]['cnt'] += 1
            if i == len(word)-1:
                cur_dict[word[i]]['end'] = word
            cur_dict = cur_dict[word[i]]
    pprint(root, depth=10)
    return root

def search_trie(trie, word):
    cur = trie
    for i in range(len(word)):
        cur = cur[word[i]]
        if cur['cnt'] == 1:
            print(123, word[:i+1])
            return i + 1
        else:
            if 'end' in cur:
                if cur['end'] == word:
                    print(123, word[:i+1])
                    return len(word)
    return len(word)

def solution(words):
    answer = 0
    trie = make_trie(words)
    for word in words:
        answer += search_trie(trie, word)
    return answer

print(solution(["go", "gone", "guild"]))
print(solution(["abc", "def", "ghi", "jklm"]))
print(solution(["word", "war", "warrior", "world"]))
