import re


def solution(dartResult):
    print(dartResult)
    groups = re.findall(r"(\d+)(\w)(\W?)", dartResult)
    print(groups)
    for index, round in enumerate(groups):
        score, bonus, option = round
        bonus = 1 if bonus == "S" else 2 if bonus == "D" else 3
        groups[index] = int(score) ** bonus
        if option == "*":
            groups[index] *= 2
            if index != 0:
                groups[index - 1] *= 2
        if option == "#":
            groups[index] = -groups[index]
    return sum(groups)


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
# print(solution("1D2S0T"))
# print(solution("1S*2T*3S"))
# print(solution("1D#2S*3S"))
# print(solution("1T2D3D#"))
# print(solution("1D2S3T*"))
