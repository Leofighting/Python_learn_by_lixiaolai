admins = {"Moose","Joker","Joker"}
moderators = {"Ann","Chris","Jane","Moose","Zero"}

print(admins)
print("Joker" in admins)
print("Joker" in moderators)
print(admins | moderators)
print(admins & moderators)
print(admins - moderators)
print(admins ^ moderators)
