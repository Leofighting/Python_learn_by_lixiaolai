def say_hi(*names):

    for name in names:
        print(f"Hi, {name}!")


a_string = "Python"
print(say_hi(*a_string))

a_range = range(10)
print(say_hi(*a_range))

a_list = list(range(10, 0, -1))
print(say_hi(*a_list))

a_dictionary = {"ann": 2321, "mike": 8712, "joe": 7610}
print(say_hi(*a_dictionary))
