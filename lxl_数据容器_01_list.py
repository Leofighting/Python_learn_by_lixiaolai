import random
# a_list = []
# a_list.append(1)
# a_list.append(2)
# print(a_list,f"has a length of {len(a_list)}.")
#
# b_list = list(range(1,9))
# b_list.append(11)
# print(b_list,f"has a length of {len(b_list)}.")
#
# c_list = [2**x for x in range(8)]
# print(c_list,f"has a length of {len(c_list)}.")
#
# n = 10
# a_list = [random.randrange(1,100) for i in range(n)]
# b_list = [x for x in a_list if x % 2 == 0]
# print(f"a_list comprehends {len(a_list)} random numbers:{a_list}")
# print(f"...and it has {len(b_list)} even numbers: {b_list}")

n = 3
a_list = [random.randrange(65,91) for i in range(n)]
b_list = [chr(random.randrange(65,91)) for i in range(n)]
print(a_list)
c_list = a_list + b_list + a_list * 2
print(c_list)

print()

print(c_list[3])
print(c_list[:])
print(c_list[5:])
print(c_list[:3])
print(c_list[2:6])

print()

del c_list[3]
print(c_list)

del c_list[5:8]
print(c_list)

print()

c_list[1:5:2] = ["a",2]

print(c_list)
#
# print("-" * 30)
#
# s = "Python"[2:5]
# print(s)
#
# L = list(s)
# print(L)
# del L[2]
# print(L)

a_list *= 3
print(a_list)
print(len(c_list))
print(max(b_list))
print(min(b_list))

print("X" not in b_list)