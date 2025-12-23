# ------------------------
# -- Set Methods Part 3 --
# ------------------------

# those methods retuan boolean values (True - False)

# issuperset()

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}
print(a.issuperset(b))  # True
# is b elements exest in a ?

print(a.issuperset(c))  # False => all elemens must be exest
# is c elements exest in a ?

print("=" * 45)

# issubset()

d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}

print(d.issubset(e))  # False
# is d elements exest in e ?
# note : all set elements must be exested
print(d.issubset(f))  # True

print("=" * 45)

# isdisjoint()

g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}

print(g.isdisjoint(h))  # False
# is set g is disjoint of set h ?
print(i.isdisjoint(g))  # True

print("=" * 45)


