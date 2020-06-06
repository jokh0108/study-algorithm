def solution(user_input):
    lower, upper, digit, special, long_enough = [0] * 5
    for c in user_input:
        if c.isdigit():
            digit = 1
        elif c.isalpha() and c.isupper():
            upper = 1
        elif c.isalpha() and c.islower():
            lower = 1
        else:
            special = 1
    if len(user_input) >= 10:
        long_enough = 1
    level = sum([lower, upper, digit, special, long_enough])
    return f'LEVEL{level}'


print(solution('adfkdncjdk'))
print(solution('Aei0#'))
print(solution('aq%~9P2!@@s!v#&&KM^lFf'))
