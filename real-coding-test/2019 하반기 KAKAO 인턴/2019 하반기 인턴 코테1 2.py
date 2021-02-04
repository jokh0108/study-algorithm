import pprint

def solution(board, moves):
    # pprint.pprint(board)
    # print(moves)
    stack = []
    answer = 0
    n = len(board)
    for mov in moves:
        for i in range(n):
            if board[i][mov - 1] != 0:
                stack.append(board[i][mov - 1])
                if len(stack) >= 2 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
                board[i][mov - 1] = 0
                # pprint.pprint(board)
                # print(i, mov - 1, stack)
                break

    return answer

a = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
print(a)