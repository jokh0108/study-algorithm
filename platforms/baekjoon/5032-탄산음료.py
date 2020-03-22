e, f, c = map(int, input().split())
e = e + f
soda = 0
while e >= c:
    new = e // c
    soda += new
    # print(e,"->",  new)
    e = e % c + new
print(soda)