N = int(input())
num = 665
count = 0

while True:
    num += 1
    if str(num).find("666") >= 0:
        count += 1
    if count == N:
        print(num)
        break
