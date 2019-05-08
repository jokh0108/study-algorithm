from collections import deque
from copy import deepcopy


def findRoute(ans, tickets, lst, start, next_airport):
    lst.append(next_airport)
    # print(lst)
    idx = tickets.index([start, next_airport])
    del tickets[idx]
    if not tickets:
        ans.append(deepcopy(lst))
        return 0
    for i in range(len(tickets)):
        if tickets[i][0] == next_airport:
            findRoute(ans, deepcopy(tickets), lst, next_airport, tickets[i][1])
            lst.pop()
            # print(lst)


def solution(tickets):
    tickets = deque(tickets)
    ans = []
    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            tickets_copy = deepcopy(tickets)
            findRoute(ans, tickets_copy, ["ICN"], "ICN", tickets[i][1])
    # print("ans", ans)
    m = ['ZZZ']*10001
    for each in ans:
        if "".join(m) > "".join(each):
            m = each
    return m

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
