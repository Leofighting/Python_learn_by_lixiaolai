# for i in range(3):
#     print(i)
#
# for i in [1,2,3]:
#     print(i)
#
# s = "Python"
# for i,c in enumerate(s):
#     print(i,c)
#
# for i,v in enumerate(range(3)):
#     print(i,v)
#
# l = ["ann","bob","joe","john","mike"]
# for i,l in enumerate(l):
#     print(i,l)
#
# t = ("ann","bob","joe","john","mike")
# # for i,t in enumerate(t):
# #     print(i,t)
#
# for i,t in enumerate(sorted(t,reverse=True)):
#     print(i,t)
#
# chars = 'abcdefghijklmnopqrstuvwxyz'
# nums = range(1,27)
# for c,n in zip(chars,nums):
#     print(f"Let's assume {c} represents {n}")

phonebook1 = {"ann":6575,"bob":8982,"joe":2598,"zoe":1225,"ann":6585}

# for key in phonebook1:
#     print(key,phonebook1[key])

for key,value in phonebook1.items():
    print(key,value)

