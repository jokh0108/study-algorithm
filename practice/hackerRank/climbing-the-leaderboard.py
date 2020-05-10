
def binary_search(arr, x):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return (True, mid)
        elif arr[mid] > x:
            right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
    # not found
    if mid == 0 and x < arr[mid]:
        return (False, -1)
    elif mid == len(arr)-1 and x > arr[mid]:
        return (False, len(arr))
    else:
        if x < arr[mid]:
            return (False, mid)
        else:
            return (False, mid+1)

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    rank = 1
    board = {}
    for score in scores:
        if score not in board:
            board[score] = rank
            rank += 1
    # print(board)
    score_ascending = sorted(board.keys())
    # print(score_ascending)

    answers = []
    for alice_score in alice:
        is_found, idx = binary_search(score_ascending, alice_score)
        # print(is_found, idx, alice_score)
        if is_found:
            answers.append(board[score_ascending[idx]])
        else:
            if idx == -1:
                answers.append(len(score_ascending)+1)
            elif idx == len(score_ascending):
                answers.append(1)
            else:
                alice_rank = board[score_ascending[idx]] + 1
                answers.append(alice_rank)

    return answers
