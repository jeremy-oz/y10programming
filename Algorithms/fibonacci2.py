def fin(n):
    f = [0, 1, 1]
    if n >= 2:
        for i in range(2, n):
            f.append(f[i] + f[i-1])
    elif n == 1:
        f = [0, 1]
    elif n == 0:
        f = [0]
    return f

print(fin(500))

