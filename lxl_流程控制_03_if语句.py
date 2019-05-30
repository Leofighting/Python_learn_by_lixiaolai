import random

r = random.randrange(0,13)

if r == 7:
    print(r)
    print("Draw!")
elif r >= 2 and r < 7:
    print(r)
    print("Small")
elif r > 7:
    print(r)
    print("Big!")
else:
    print("Not valid!")