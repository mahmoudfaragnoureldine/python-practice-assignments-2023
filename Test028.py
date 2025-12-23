# ------------------------
# -- Set Methods Part 2 --
# ------------------------

# difference()

a = {1, 2, 3, 4}
b = {1, 2, "Walid", "Ahmed"}
print(a) # {1, 2, 3, 4}
print(a.difference(b)) # a - b  => {3, 4}
print(a) # {1, 2, 3, 4}

print("=" * 40)  # separator

# difference_update()

c = {1, 2, 3, 4}
d = {1, 2, "Walid", "Ahmed"}
print(c) # {1, 2, 3, 4}
c.difference_update(d) # 
print(c) # {3, 4}

print("=" * 40)  # separator

# # intersection()

e = {1, 2, 3, 4, "X", "Walid"}
f = {"Walid", "X", 2}
print(e)  # {1, 2, 3, 4, 'Walid', 'X'}
print(e.intersection(f))  # e & f  => {'Walid', 2, 'X'}
print(e)  # {1, 2, 3, 4, 'Walid', 'X'}

print("=" * 40)  # separator

# intersection_update()

g = {1, 2, 3, 4, "X", "Walid"}
h = {"Walid", "X", 2}
print(g)  # {1, 2, 3, 4, 'Walid', 'X'}
g.intersection_update(h)   # g & h  
print(g)  # {2, 'Walid', 'X'}

print("=" * 40)  # separator

# symmetric_diffreence()

i = {1, 2, 3, 4, 5, "X"}
j = {"Walid", "Zero", 1, 2, 4, "X"}
print(i)  # {1, 2, 3, 4, 5, 'X'}
print(i.symmetric_difference(j))  # i ^ j => {'Walid', 3, 5, 'Zero'}
print(i)  # {1, 2, 3, 4, 5, 'X'}

print("=" * 40)  # separator

# symmetric_diffreence_update()

k = {1, 2, 3, 4, 5, "X"}
l = {"Walid", "Zero", 1, 2, 4, "X"}
print(k)  # {1, 2, 3, 4, 5, 'X'}
k.symmetric_difference_update(l)  # k ^ l
print(k)  # {3, 5, 'Zero', 'Walid'}

print("=" * 40)  # separator
