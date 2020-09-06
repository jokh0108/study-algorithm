from collections import defaultdict
from pprint import pprint



def dfs(start, end, answer, path, visited):
    # print(start, end)
    answer.append(end)
    visited[(start, end)] = True
    pprint(visited, width=20)
    for next_end in path[end]:
        if not visited[(end, next_end)]:
            dfs(end, next_end, answer, path, visited)

def solution(tickets):
    path = defaultdict(list)
    visited = defaultdict(bool)
    for start, end in tickets:
        path[start].append(end)
        visited[(start, end)] = False

    for start in path.keys():
        path[start] = sorted(path[start])
    answer = ["ICN"]
    # pprint(path, width=20)
    # pprint(visited, width=20)
    dfs("ICN", path["ICN"][0], answer, path, visited)

    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(	["ICN", "JFK", "HND", "IAD"] == solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
print(	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] == solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))