# ---------
# -- Set --
# ---------
# [1] Set items enclosed in curly braces
# [2] Set items are not ordered and not indexed
# [3] Set Indexing and Slicing cannot be done
# [4] Set has only immutable data (numbers, string, tuples) list and dict are not
# [5] set items is Unique
# -------------------------------------------

# Not ardered and not indexed

mySet1= {"Walid", "Ahmed", 100}
print(mySet1)
#print(mySet1[0])

# Slicing cannot be done

mySet2 = {1, 2, 3, 4, 5}
#print(mySet2[0:3])  # TypeError: 'set' object is not subscriptable     

# Has only immutablr data

#mySet3 = {"Walid", 100, 100.5, True, [1, 2, 3]} # unhashable type: 'list'
#print(mySet3)

# items is unique

myset4 = {1, 2, "Walid", "One", "Walid", 1}
print(myset4)  # {'Walid', 1, 2, 'One'}

