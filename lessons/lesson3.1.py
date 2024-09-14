a = [1, 2, 3]
b = a.copy()
print(id(a), id(b))
print(a, b)
a.append(4)
print(a, b)



