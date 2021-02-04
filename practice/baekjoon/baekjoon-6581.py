import sys

while True:
    input_ = sys.stdin.readline()
    if input_ == '':
        break
    print(input_)
    sys.stdout.write(input_)