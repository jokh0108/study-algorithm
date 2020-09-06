exp = input()
atom = []
j = 0 
for i in range(len(exp)):
    # print(exp[i])
    if exp[i].isdigit():
        if exp[i] != '1':
            atom[j] += exp[i]
        j += 1
    else:
        if exp[i].isupper():
            atom.append(exp[i])
        if exp[i].islower():
            atom[-1] += exp[i]
if j != len(atom):
    print("error")
else:
    print("".join(atom))