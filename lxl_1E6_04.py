n = 10000
a = range(n)
b = tuple(a)
c = list(a)
a = a.__sizeof__()
b = b.__sizeof__()
c = c.__sizeof__()

print(a,b,c)