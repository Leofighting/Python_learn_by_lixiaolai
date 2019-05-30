import random
n = 3
a_list = [random.randrange(65,91) for i in range(n)]
b_list = [chr(random.randrange(65,91)) for i in range(n)]
print(a_list)
c_list = a_list + b_list + a_list * 2

c_list.append("100")
print(c_list)

print()
print(a_list)
a_list.clear()
print(a_list)

print()
d_list = c_list.copy()
print(d_list)
del d_list[6:8]
print(d_list)
print(c_list)

print()
print(a_list)
a_list.extend(c_list)
print(a_list)

print()
print(a_list)
a_list.insert(1,"example")
a_list.insert(3,"example")
print(a_list)

print()
print(a_list)
a_list.reverse()
print(a_list)
x = a_list.reverse()
print(x)