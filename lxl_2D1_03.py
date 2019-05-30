def fib_between(start,end):
    # a,b = 0,1
    # while a < end:
    #     if a >= start:
    #         print(a,end=" ")
    #     a,b = b,a+b


    r = []
    a,b = 0,1
    while a < end:
        if a >= start:
            r.append(a)
        a,b = b,a+b
    return r

print(fib_between(100,10000))