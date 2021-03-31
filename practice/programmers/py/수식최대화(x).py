import itertools


def solution(expression):
    OPERATORS = ("+", "-", "*")
    answer = 0
    operand = ""
    new_exp = []
    for i, c in enumerate(expression):
        if c.isdigit():
            operand += c
            if i == len(expression)-1:
                new_exp.append(int(operand))
        else:
            new_exp.append(int(operand))
            operand = ""
            new_exp.append(c)
    for p in itertools.permutations(OPERATORS):
        # print("p", p)
        copied_exp = new_exp[:]
        # print("copied_exp", copied_exp)
        prize = 0
        for op in p:
            while op in copied_exp:
                op_index = copied_exp.index(op)
                left = copied_exp[op_index-1]
                right = copied_exp[op_index+1]
                # print(left, right)
                new_operand = left + right
                if copied_exp[op_index] == "-":
                    new_operand = left - right
                if copied_exp[op_index] == "*":
                    new_operand = left * right
                copied_exp[op_index-1] = new_operand
                copied_exp.pop(op_index)
                copied_exp.pop(op_index)

                # print(copied_exp)
            prize = abs(copied_exp[0])
            answer = max(answer, prize)
    return answer


print(solution("100-200*300-500+20"))
# print(solution("50*6-3*2"))
