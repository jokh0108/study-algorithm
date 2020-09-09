"""
폰 넘버 리포맷
space, dash 없앤다
앞에서 부터 3개씩 자른다
각 숫자는 최소 2개 여야한다.
'00-44   48 5555 8361' -> '004-448-555-583-61'
'0 - 22 1985--324' -> '022-198-53-24'
'555372654' -> '555-372-654'
"""

def solution(S):
    compressed = "".join([c for c in S if c not in ('-', ' ')])
    print(compressed)
    grouped = [compressed[i:i+3]for i in range(0, len(compressed), 3)]
    if len(grouped[-1]) == 1:
        last1 = grouped[-1]
        last2 = grouped[-2]
        grouped[-1] = last2[-1] + last1
        grouped[-2] = last2[:2]
    print(grouped)
    return "-".join(grouped)


print(solution('00-44   48 5555 8361'))
print(solution('0 - 22 1985--324'))
print(solution('555372654'))
