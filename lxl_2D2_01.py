def say_hi(*names):
    for name in names:
        print(f"Hi,{name}")


names = ("mike", "joe", "john")
print(say_hi(*names))

# print(say_hi("ann"))
# print(say_hi("mike", "joe", "john"))
