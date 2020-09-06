def getRowWord(i, j):
    return board[i][j:j+N]

def getColWord(i, j):
    return "".join([board[i+k][j] for k in range(N)])

def isPal(word):
    length = len(word)
    if length % 2 == 0:
        if word[:length//2] == word[:length//2-1:-1]:
            return True
        else:
            return False
    else:
        if word[:length//2] == word[:length//2:-1]:
            return True
        else:
            return False


def findPalindrome():
    cnt = 0 
    for i in range(8):
        for j in range(9-N):
            word = getRowWord(i, j) 
            if isPal(word):
                cnt += 1
    for i in range(9-N):
        for j in range(8):
            word = getColWord(i, j) 
            if isPal(word):
                cnt += 1
    return cnt

for i in range(1, 11):
    N = int(input())
    board = [input() for _ in range(8)]
    ans = findPalindrome()

    print("#%d"%i, ans)
