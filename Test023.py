# -------------------
# -- Lists Methods --
# -------------------

# clear بتشيل كل العماصر الموجوده فى الليست
# ملاحظه انت بتفضيها مش بتحذفها
a = [1, 2, 3, 4]
a.clear()
print(a) 

# copy()

b = [1 ,2 ,3 ,4]
c = b.copy()     # shaloCopy
print(b)  # main list [1, 2, 3, 4]
print(c)  # copied list [1, 2, 3, 4]

b.append(5)

print(b)  # main list [1, 2, 3, 4, 5]
print(c)  # copied list [1, 2, 3, 4]

# count()

d = [1, 2, 3, 4, 9, 10, 1, 2, 1]
print(d.count(1))  # 3

# index()

e = ["walid", "ahmed", "sayed", "ramy", "ahmed", "ramy"]
print(e.index("ramy"))

# insert() 
f = [1, 2, 3, 4]
f.insert(0, "test")
f.insert(-1, "test")
print(f)   # ['test', 1, 2, 3, 'test', 4]

# pop() 

g = [1, 2, 3, 4, 5, "a", "b"]
print(g.pop(-1))  # b

