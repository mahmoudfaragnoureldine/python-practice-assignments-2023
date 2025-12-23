# -----------
# -- Lists -- بتادى نفس وظيفة الاراى لكنها مش اراى
# -----------
# [1] List item is enclosed in sqaure brackets
#myAwesomeList = []
# [2] List are ordered to use to access item
# [3] List are mutable => add, delete, edit 
# [4] List item is not unique
#myAwesomeList = ["one", "two", "one"]
# [5] List can have different data types
myAwesomeList = ["one", "two", "one", 1, 100.5, True]

print(myAwesomeList)
print(myAwesomeList[1])
print(myAwesomeList[-1])

print(myAwesomeList[1:4]) # ['two', 'one', 1]
print(myAwesomeList[:4]) # ['one', 'two', 'one', 1]
print(myAwesomeList[1:]) # ['two', 'one', 1, 100.5, True] 

print(myAwesomeList[::1]) # ['one', 'two', 'one', 1, 100.5, True]
print(myAwesomeList[::2]) # ['one', 'one', 100.5]

# myAwesomeList[1] = 2
# myAwesomeList[-1] = False
# myAwesomeList[0:3] = [] # deleted
myAwesomeList[0:3] = ["A", "B", "C"] # ['A', 'B', 'C', 1, 100.5, True]
print(myAwesomeList)


