# from itertools import product

# # 모든 경우의 수 - 불가능한 경우의 수
# def check(string):
#     stack = []
#     for each in string:
#         if each == '(':
#             stack.append(each)
#         else:
#             if stack == []:
#                 return False
#                 break
#             left = stack.pop()
#     if stack != []:
#         return False
#     else:
#         return True


def solution(N):
    answer = []
    # # 중복 순열로 모든 케이스 check
    # for each in product(['(',')'],  repeat = N*2):
    #     each = "".join(each)
    #     # print(each)
    #     if check(each):
    #         answer.append(each)            
    # return answer
    answer = [ [""] ]
    
    for i in range(N):
        s = set()        
        for each in answer[i]:
            parenthesis = each
            s.add('(' + parenthesis + ')')
            s.add(parenthesis + '()')
            s.add('()' + parenthesis)
        answer.append(sorted(list(s)))
    print(*answer, sep = '\n')
    


# print(solution(	2))
print(solution(	5))
