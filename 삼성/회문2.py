def getRowWord(i, j, k):
    return board[i][j:j+k]

def getColWord(i, j, k):
    return "".join([board[i+n][j] for n in range(k)])

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


def findMaxPalindrome():
    M = 0
    for i in range(100):
        for j in range(100):
            for k in range(1,101 - j):
                word = getRowWord(i, j, k) 
                if isPal(word):
                    if M < len(word):
                        M = len(word)
    for i in range(100):
        for j in range(100):
            for k in range(1,101 - i):
                word = getColWord(i, j, k) 
                if isPal(word):
                    if M < len(word):
                        M = len(word)
    return M

for i in range(1, 11):
    input()
    board = [input() for _ in range(100)]
    ans = findMaxPalindrome()

    print("#%d"%i, ans)
