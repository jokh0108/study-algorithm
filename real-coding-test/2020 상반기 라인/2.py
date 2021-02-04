from itertools import combinations

def solution(answer_sheet, sheets):
    answer = 0
    for a, b in combinations(sheets, 2):
        arr = [0]*len(answer_sheet)
        # print(a, b)
        # print(arr)
        M = 0
        cnt = 0
        for i in range(len(answer_sheet)):
            # print(a[i], b[i], answer_sheet[i], (a[i] == b[i]), (a[i] != answer_sheet[i]))
            if (a[i] == b[i]) and (a[i] != answer_sheet[i]):
                cnt += 1
                if i == 0:
                    arr[i] = 1
                else:
                    arr[i] = arr[i-1] + 1
            if M < arr[i]:
                M = arr[i]
        if answer < cnt + M**2:
            answer = cnt + M**2
    return answer

print(solution("4132315142", ["3241523133", "4121314445", "3243523133", "4433325251", "2412313253"]))
print(solution("53241", ["53241", "42133", "53241", "14354"]))
print(solution("24551", ["24553", "24553", "24553", "24553"]))