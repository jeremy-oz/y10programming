def fin(n):
    if n > 2:
        return fin(n-1) + fin(n-2)
    elif n == 2:
        return 1
    elif n == 1:
        return 0

for i in range(2, 20):
    print(fin(i), end=' ')


# 0 1 1 2 3 5 8