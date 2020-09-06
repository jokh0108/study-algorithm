# 15- 25
def solution(board, moves):
    moves = list(map(lambda x: x-1, moves))
    print(*board, moves, sep='\n')
    st = []
    cnt = 0
    for m in moves:
        for i in range(len(board)):
            if board[i][m] != 0:
                if st and st[-1] == board[i][m]:
                    st.pop()
                    cnt += 2
                else:
                    st.append(board[i][m])
                board[i][m] = 0
                break
    return cnt

print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))