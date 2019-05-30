import random
n = 3
a_list = [random.randrange(65,91) for i in range(n)]
print(a_list)

print()
a_list.insert(1,"example")

print()
print(a_list)
a_list.remove("example")
print(a_list)

print()
print(a_list)
p = a_list.pop(2)
print(a_list)
print(p)

print()
a_list.insert(2,"example")
a_list.insert(2,"example")
print(a_list)
del a_list[2]
print(a_list)

print()
print(a_list.remove("example"))
print(a_list)
