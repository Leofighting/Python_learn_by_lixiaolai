for n in range(2,100):
    if n == 2:
        print(n)
        continue
    for i in range(2,n):
        if (n % i) == 0:
            break
    else:
        print(n)

