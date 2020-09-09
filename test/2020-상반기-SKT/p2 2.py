"""
string(a-z)이 주어졌을 때 'a'가 연속으로 3개가 안되도록 a를 넣어줌
'aabab' -> 'aabaabaa', return 3
'dog' -> 'aadaaoaagaa', return 8
'aa' -> 'aa', return 0
'baaaa' -> return -1


"""

def solution(S):
    inserting_a = 0
    arr = []
    count = 0
    for i in range(len(S)):
        if S[i] == 'a':
            inserting_a += 1
            if inserting_a >= 3:
                return arr, -1
        else:
            arr.append(inserting_a)
            arr.append(S[i])
            count += 2 - inserting_a
            inserting_a = 0

        if i == len(S)-1:
            if S[i] == 'a':
                arr.append(inserting_a)
                count += inserting_a
            else:
                arr.append(0)
                count += 2
    print(arr, f'{count}')

print(solution('aabab'))
print(solution('dog'))
print(solution('aa'))
print(solution('baaaa'))
