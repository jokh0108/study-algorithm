def noteToList(note):
    listened = []
    for j in range(len(note)):
        if note[j] != '#':
            listened.append(note[j])
        else:
            listened[-1] += '#'
    return listened

def solution(m, musicinfos):
    answer = []
    for i in range(len(musicinfos)):
        start, end, title, note = musicinfos[i].split(',')
        duration = ((int(end[:2]))*60 + int(end[3:])) - \
            ((int(start[:2]))*60 + int(start[3:]))
        notecopy = note[:]
        played = noteToList(notecopy)
        note = played[:]
        # print(duration)
        if duration > len(played):
            j = 0
            # print(played)
            while duration > len(played):
                played.append(note[j])
                j = (j + 1) % len(note)
                # print(len(played), played)
        else:
            played = played[:duration]
            # print(played)
        listened = noteToList(m)
        for i in range(len(played) - len(listened) + 1):
            if listened == played[i: i + len(listened)]:
                answer.append({"priority": len(musicinfos)- i, "duration" : duration, "title" : title})
    answer = sorted(answer, key=lambda x: (x["duration"], x["priority"]), reverse=True)
    if not answer:
        return '(None)'
    return answer[0]["title"]


print(
    solution("A", ["00:00,00:09,HELLO,"+"BB", "13:00,13:04,WORLD,AB", "13:00,13:04,SHIT,ABC"]))
print(
    solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", [
      "03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(
    solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
