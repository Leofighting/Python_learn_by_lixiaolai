phonebook1 = {"ann":6575,"bob":8982,"joe":2598,"zoe":1225,"ann":6585}

# print(phonebook1["joe"])
#
# phonebook1["joe"] = 5802
# print(phonebook1)
# print(phonebook1["joe"])

phonebook2 = {"john":9876,"mike":5603,"stan":6898,"eric":7898}
#
# phonebook1.update(phonebook2)
# print(phonebook1)



# print("ann" in phonebook1)
#
# print(phonebook1.keys())
# print("stan" in phonebook1.keys())
#
# print(phonebook1.values())
# print(1225 in phonebook1.values())
#
# print(phonebook1.items())
# print(("stan",6898) in phonebook1.items())
#
# print(phonebook1.update(phonebook2))
#
# print(len(phonebook1))
# print(max(phonebook1))
# print(min(phonebook1))
# print(list(phonebook1))
# print(tuple(phonebook1))
# print(set(phonebook1))
# print(sorted(phonebook1))
# print(sorted(phonebook1,reverse=True))

phonebook3 = phonebook2.copy()
print(phonebook3)

phonebook3.clear()
print(phonebook3)

print(phonebook2)

p = phonebook1.pop("adam",3538)
print(p)
print(phonebook1)

p = phonebook1.get("adam",3538)
print(p)
print(phonebook1)

p = phonebook1.setdefault("adam",3538)
print(p)
print(phonebook1)

