from collections import defaultdict
from pprint import pprint
def solution(genres, plays):
    answer = []
    total = defaultdict(int)
    count = defaultdict(list)
    # dic = defaultdict(lambda : defaultdict(int))
    for i in range(len(genres)):
        # dic[genres[i]][i] += plays[i]
        # pprint(dic, width = 20)
        total[genres[i]] += plays[i]
        count[genres[i]].append((i, plays[i]))
    # pprint(total,width = 20)    
    # pprint(count,width = 20)    
    total = sorted(total, reverse = True)
    # pprint(total,width = 20)    
    for genre in total:
        count[genre] = sorted(count[genre], reverse= True, key=lambda x:x[1])[:2]
        # print(count[genre])
        answer.extend([x[0] for x in count[genre]])
        # print(answer)
    # pprint(count,width = 20)    
    return answer

print(solution(	["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
