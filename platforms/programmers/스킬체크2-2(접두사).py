from pprint import pprint
from collections import deque

def bfs(T):
    q = deque()
    for key in T.keys():
        q.append(key)
        T[key]["visited"] = 1

    curr = T
    while q:
        key = q.popleft()
        if curr.get(key):
            curr = curr[key]
        else:
            continue
        temp = []
        if curr.get("last"):
            return False
        for child in curr.keys():
            if child.isdigit():
                q.append(child)
                if not curr[child].get("visited"):
                    curr[child]["visited"] = 1
    return True
        

    

def solution(phone_book):
    answer = True
    T = {}
    for phone_num in phone_book:
        curr = T
        for i in range(len(phone_num)):
            if not curr.get(phone_num[i]):
                curr[phone_num[i]] = {}
            curr = curr[phone_num[i]]
            if i == len(phone_num) - 1:
                curr["last"] = True
    
    return bfs(T)


print(solution(["911", "97625999", "91125426"]))
print(solution(["113", "12340", "123440", "12345", "98346"]))
print(solution(["12232332", "12", "222222"]))
