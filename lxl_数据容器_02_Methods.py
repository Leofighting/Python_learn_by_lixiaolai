import random
n = 10
a_list = [random.randrange(1,100) for i in range(n)]
print(f"a_list comprehends {len(a_list)} random number:\n",a_list)

a_list.sort()
print("the list sorted:\n",a_list)

a_list.sort(reverse=True)
print("the list sorted reversely:\n",a_list)

# 第二个程序

a_list = [chr(random.randrange(65,91)) for i in range(n)]
print(f"a_list comprehends {len(a_list)} random string elements:\n",a_list)

a_list.sort()
print("the list sorted:\n",a_list)

a_list.sort(reverse=True)
print("the list sorted reversely:\n",a_list)

print("-" * 30)

b_list = [chr(random.randrange(65,91)) + \
          chr(random.randrange(97,123))\
          for i in range(n)]
print(f"b_list comprehends {len(b_list)} random string elements:\n",b_list)

b_list.sort()
print("the sorted:\n",b_list)

b_list.sort(key=str.lower,reverse=True)
print("the sorted reversely:\n",b_list)