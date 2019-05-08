def check(string):
    stack = []
    for each in string:
        if each == '(':
            stack.append(each)
        else:
            if stack == []:
                return "NO"
                break
            left = stack.pop()
    if stack != []:
        return "NO"
    else:
        return "YES"

t = int(input())
for _ in range(t):
    string = input()
    print(check(string))