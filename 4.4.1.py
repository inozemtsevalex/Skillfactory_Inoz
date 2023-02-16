def p(n):
    if n == 0:
        return
    else:
        p(n-1)
        print(n)
p(5)