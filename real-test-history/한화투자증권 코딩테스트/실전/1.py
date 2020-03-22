# https://www.slideshare.net/NaverEngineering/ss-97817579

result = []

while True:
    line = input()
    if not line:
        break
    # cat -> 출력을 의미
    # grep -> 파일에서 특정 패턴 찾는 명령어
    # grep "^Google" -> "Google"로 시작하는 문자열을 찾는다
    # grep -v "Apple" -> "Apple"이 문자열에 포함되면 제외시킨다.
    if line[:len("Google")] == "Google" and "Apple" not in line:
        result.append(line)
print(len(result))