print("Example of str.find():")
s = """Simple is better than complex.
Complex is better than complicated."""
a = s.lower().find("mpl")
b = s.lower().find("mpl",10)
c = s.lower().find("mpl",10,20)
print(a,b,c)

print("Example of str.rfind():")
s.lower().rfind("mpl")plicated
s.lower().rfind("mpl",10)
s.lower().rfind("mpl",10,20)
print()

print("Example of str.index():")
s.lower().index("mpl")
s.lower().rindex("mpl")
print()


