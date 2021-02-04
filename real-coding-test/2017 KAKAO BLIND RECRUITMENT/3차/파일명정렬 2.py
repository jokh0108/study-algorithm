def solution(files):
    for i in range(len(files)):
        j = 0
        while not files[i][j].isdigit():
            j += 1
        k = j
        while k < len(files[i]) and files[i][k].isdigit():
            k += 1
        HEAD = files[i][:j]
        NUMBER = files[i][j:k]
        TAIL = files[i][k:]
        # print(HEAD, NUMBER, TAIL)
        files[i] = [HEAD, NUMBER, TAIL] 
    # print(files)
    files = sorted(files , key = lambda x : (x[0].upper(),int(x[1])))
    # print(files)
    for i in range(len(files)):
        files[i] = "".join(files[i])
    return files

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))