cr = ['c=','c-','dz=','d-','lj','nj','s=','z=']

word = input()
cnt =0
while word:
    alpha = word[-2:]
    #print(word, alpha, cnt)
    cnt += 1

    if alpha not in cr:
        word = word[:-1]
        continue
    else:
        if alpha == 'z=':
            if len(word) == 2:
                break
            elif len(word) == 3:
                if word[-3] == 'd':
                    break
            elif len(word) > 3:
                if word[-3] == 'd':
                    word = word[:-3]
                    continue
    word = word[:-2]
print(cnt)