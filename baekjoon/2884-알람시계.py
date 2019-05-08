H, M = map(int, input().split())
t = H * 60 + M
alarm = (t-45) % (24*60)
print(alarm//60, alarm % 60)