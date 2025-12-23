# ------------------------
# -- Set Methods Part 1 --
# ------------------------

# clear()

a ={1, 2, 3}
a.clear()
print(a)  # set()

# union()

b = {"one", "two", "three"}
c = {"1", "2", "3"}
x = {"zero", "cool"}

print(b | c)  # {'two', '3', '2', '1', 'one', 'three'}
print(b.union(c))
print(b.union(c, x)) 

# add()

d = {1, 2, 3, 4}
d.add(5)
print(d) # {1, 2, 3, 4, 5}

# copy()

e = {1, 2, 3, 4}
f = e.copy()   # shaloCopy
print(f)   # {1, 2, 3, 4}

# remove()

g = {1, 2, 3, 4}
g.remove(1)
#g.remove(7)  # Error
print(g)  # {2, 3, 4}

# discard() 

h = {1, 2, 3, 4}
h.discard(1)
h.discard(7)
print(h)  # {2, 3, 4}

# pop()
i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop()) # random element

# update()

j = {1, 2, 3}
k = {1, "a", "b", 2}
j.update(['Html', 'Css'])
j.update(k)

print(j)  # {1, 2, 3, 'Html', 'b', 'Css', 'a'}




