# ------------
# -- Tuples --
# ------------
# [1] Tuple item are enclosed in parentheses
# [2] you can remove the parentheses if you want
# [3] Tuple are ordered, to use Index to access item
# [4] Tuple is immutable => you cannot add or delete
# [5] Tuple Items os not Unique
# [6] Tuple can have different data types
# [7] Opperators used in string and list avaliable in tuples
# --------------------------

# Tuole Syntax & Type Test

myTuple1 = ("Walid", "Ahmed") 
myTuple2= "Walid", "Ahmed"

print(myTuple1)
print(myTuple2)

print(type(myTuple1))
print(type(myTuple2))

# Tuple Index 

myTuple3 = (1, 2, 3, 4, 5)
print(myTuple3[0]) # 1
print(myTuple3[-1]) # 5
print(myTuple3[-3]) # 3

# Tuple Assign Values

myTuple4 = (1, 2, 3, 4, 5)
#myTuple3[2] = "Walid"
#print(myTuple3)  # tuple' object does not support item assignment

# Tuple items

myTuple5 = ("Walid", "Walid", 1, 2, 3, 100.5, True) 
print(myTuple5[1])  # Walid
print(myTuple5[-1]) # True





