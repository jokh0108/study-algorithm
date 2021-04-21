N = int(input())

answer = 10 ** 8
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        for g in range(10):
                            if (
                                ((10 ** 6 + 1) * a)
                                + ((10 ** 5 + 1) * b)
                                + ((10 ** 4 + 1) * c)
                                + ((10 ** 3 + 1) * d)
                                + ((10 ** 2 + 1) * e)
                                + ((10 ** 1 + 1) * f)
                                + ((10 ** 0 + 1) * g)
                            ) == N:
                                gen = (
                                    (10 ** 6) * a
                                    + (10 ** 5) * b
                                    + (10 ** 4) * c
                                    + (10 ** 3) * d
                                    + (10 ** 2) * e
                                    + (10 ** 1) * f
                                    + (10 ** 0) * g
                                )
                                answer = min(answer, gen)

if answer == 10 ** 8:
    print(0)
else:
    print(answer)
