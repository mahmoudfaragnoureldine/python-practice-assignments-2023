# ---------------------
# -- Type Conversion --
# ---------------------

# نحول انواع البيانات من نوع لنوع
# str() bult in function

a = 10
print(type(a))      # <class 'int'>
print(type(str(a))) # <class 'str'>

print('=' *45)

# tuples()

c = "Walid" # srring
d = [1, 2, 3, 4, 5] # List
e = {"a", "b", "c"} # Set
f = {"a": 1, "b": 2} # Dictionary

print(tuple(c)) # ('W', 'a', 'l', 'i', 'd')
print(tuple(d)) # (1, 2, 3, 4, 5)
print(tuple(e)) # ('a', 'b', 'c')
print(tuple(f)) # ('a', 'b')

print('=' *45)

# list()

c = "Walid" # srring
d = (1, 2, 3, 4, 5) # Tuple
e = {"a", "b", "c"} # Set
f = {"a": 1, "b": 2} # Dictionary

print(list(c)) # ['W', 'a', 'l', 'i', 'd']
print(list(d)) # [1, 2, 3, 4, 5]
print(list(e)) # ['a', 'b', 'c']
print(list(f)) # ['a', 'b']

print('=' *45)

# set()

c = "Walid" # srring
d = (1, 2, 3, 4, 5) # Tuple
e = ["a", "b", "c"] # List
f = {"a": 1, "b": 2} # Dictionary

print(set(c)) # {'i', 'W', 'l', 'a', 'd'}
print(set(d)) # {1, 2, 3, 4, 5}
print(set(e)) # {'b', 'c', 'a'}
print(set(f)) # {'b', 'a'}

print('=' *45)

# dict()

d = (("a", 1), ("b", 2), ("c", 3)) # Tuple # لازم كي وفاليو
e = [["a", 1], ["b", 2], ["c", 3]] # List

print(dict(d)) # {'a': 1, 'b': 2, 'c': 3}
print(dict(e)) # {'a': 1, 'b': 2, 'c': 3}

print('=' *45)