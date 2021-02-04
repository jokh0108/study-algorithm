from itertools import combinations
from collections import defaultdict
def checkMinimal(minimality, each):
    print(minimality)
    for item in minimality.items():
        print(k, v, each)
def solution(relation):
    minimality = defaultdict(bool)
    answer = 0
    row_len = len(relation)
    col_len = len(relation[0])
    cases = []
    for i in range(1, col_len+1):
        for each in combinations(range(col_len), i):
            cases.append(each)
    for each in cases:
        if checkMinimal(minimality, each):
            continue
        # print(each)
        s = set()
        for j in range(row_len):
            s.add(tuple([relation[j][k] for k in each]))
            # print(s)
        if len(s) == row_len:  
            # print(each)
            minimality[tuple(each)]= True
            answer += 1
    return answer
print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
# print(solution([[1,2,3,4,5,6,7,8]]))