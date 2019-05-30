a = "abcabcdeabcdbcdef"
b = range(10)
c = [1,2,2,3,3,1]
d = ('a', 'b', 'e', 'b', 'a')
print(set(a))
print(set(b))
print(set(c))
print(set(d))

b = {x for x in a if x not in "abc"}
print(b)
