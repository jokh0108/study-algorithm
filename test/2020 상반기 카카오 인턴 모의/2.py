# 25-40m
def solution(s):
    no_duplicate = s[2:-2].split('},{')
    no_duplicate = sorted([set(map(int, (x.split(',')))) for x in no_duplicate], key=lambda y: len(y))
    answer = [(no_duplicate[i]-no_duplicate[i-1]).pop() for i in range(1, len(no_duplicate))]
    return [no_duplicate[0].pop()] + answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
