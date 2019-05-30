# def say_hi(**names_greetings):
#     for name, greeting in names_greetings.items():
#         print(f"{greeting}, {name}!")
#
#
# print(say_hi(mike="Hello", ann="Oh,my darling", john="Hi"))


def say_hi_2(**names_greetings):
    for name, greeting in names_greetings.items():
        print(f"{greeting}, {name}!")


a_dictionary = {"mike":"Hello", "ann":"Oh,my darling", "john":"Hi"}
print(say_hi_2(**a_dictionary))

print(say_hi_2(**{"mike":"Hello", "ann":"Oh,my darling", "john":"Hi"}))