# def say_hi(greeting, *names):
#
#     for name in names:
#         print(f"{greeting}, {name.capitalize()}!")
#
#
# print(say_hi("Hello", "mike", "john", "zeo"))


def say_hi(greeting, *names, capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f"{greeting}, {name}!")


print(say_hi("Hello", "mike", "john", "zeo"))
print(say_hi("Hello", "mike", "john", "zeo", capitalized=False))
