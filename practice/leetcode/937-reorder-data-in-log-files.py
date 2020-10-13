
def reorderLogFiles(logs):
    letters, digits = [], []
    letters = [log for log in logs if log.split()[1].isalpha()]
    digits = [log for log in logs if log.split()[1].isdigit()]
    print(letters)
    print(digits)
    letters = sorted(letters, key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


print(reorderLogFiles(["dig1 8 1 5 1", "let1 art can",
                       "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
