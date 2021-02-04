def solution(id_list, k):
    answer = 0
    d = {}
    for row in id_list:
        targets = set(row.split())
        print(targets)
        for buyer in targets:
            if buyer not in d:
                d[buyer] = k-1
                answer += 1
            else:
                if d[buyer] > 0:
                    d[buyer] -= 1
                    answer += 1
            print(answer, d)
    return answer

print(solution(["A B C D", "A D", "A B D", "B D"], 2))
print()
print(solution(["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"], 3))