# -----------
# -- Tuple --
# -----------

# Tuple with one element

myTuple1 = ("Walid",) # without comma it will ne string
myTuple2 = "Walid",

print(myTuple1) 
print(myTuple2)

print(type(myTuple1)) 
print(type(myTuple2)) 

print(len(myTuple1))  # one element 
print(len(myTuple2)) 

# Tuple Concatenation

a = (1, 2, 3, 4)
b = (5, 6)

c = a + b 
d = a + ("a", "b", "c") + b

print(c)  # (1, 2, 3, 4, 5, 6)
print(d)  # (1, 2, 3, 4, 'a', 'b', 'c', 5, 6)

# Tuple, List, String Repeat (*)

myString = "Walid"
myList = [1, 2]
myTuple = ("a", "b")

print(myString * 6) # WalidWalidWalidWalidWalidWalid
print(myList * 6)   # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(myTuple * 6)  # ('a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b')

# Methods => count()

a = (1, 3, 7, 8, 2, 6, 5, 8)
print(a.count(8))  # 2

# Methods => Index

b = (1, 3, 7, 8, 2, 6, 5)
print(b.index(7))  # 2
print("The Postion of Index is: {:d}".format(b.index(7)))  # The Postion of Index is: 2
print("The Postion of Index is: %d" % b.index(7) )  # The Postion of Index is: 2
print(f"The Postion of Index is: {b.index(7)}" )  # The Postion of Index is: 2

# Tuple Destruct

a = ("a", "b", 4, "c")

#x, y, z = "a", "b", "c"
x, y, _, z = a

print(x) # a
print(y) # b
print(z) # c





