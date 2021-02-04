import re

def solution(new_id):
    new_id = re.sub('[^a-z0-9-_.]','', new_id.lower())
    print(new_id)
    new_id = re.sub('[.]+', '.', new_id)
    print(new_id)
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    print(new_id)
    if not new_id:
        new_id += 'a'
    print(new_id)
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id and new_id[-1] == '.':
         new_id = new_id[:-1]
    print(new_id)
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    print(new_id)

    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."	))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))