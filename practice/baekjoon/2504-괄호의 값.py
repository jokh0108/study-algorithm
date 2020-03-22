stack = []
string = list(input())

for each in string:
    temp = 0
    if each == '(' or each == '[':
        stack.append(each)
    else:
        if each == ')':
            if stack[-1] == '(':
                stack.pop()
                #check XY
                temp = 2
                if stack != [] and stack[-1].isdigit():
                    temp += int(stack.pop())
                stack.append(str(temp))
            elif stack[-1].isdigit() and stack[-2] == '(':
                temp = int(stack.pop()) * 2
                stack.pop()
                if stack != [] and stack[-1].isdigit():
                    temp += int(stack.pop())
                stack.append(str(temp))
            else:
                print(0)
                break
        elif each == ']':
            if stack[-1] == '[':
                stack.pop()
                #check XY
                temp = 3
                if stack != [] and stack[-1].isdigit():
                    temp += int(stack.pop())
                stack.append(str(temp))
            elif stack[-1].isdigit() and stack[-2] == '[':
                temp = int(stack.pop()) * 3
                stack.pop()
                if stack != [] and stack[-1].isdigit():
                    temp += int(stack.pop())
                stack.append(str(temp))
            else:
                print(0)
                break
    print(stack)
if '(' in stack or ')' in stack or '[' in stack or ']' in stack:
    print(0)
else:
    print(stack[0])