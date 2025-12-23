# -------------------
# -- Lists Methods --
# -------------------

# append() لما يكون عندى ليست وعايز اضيف ايها عنصر جديد

myFrinds = ["walid", "Mohammed", "Farag"]
myOldFrids = ["medhat", "Khalid", "Ahmed"]

myFrinds.append("Alaa") # ['walid', 'Mohammed', 'Farag', 'Alaa']
myFrinds.append(100)
myFrinds.append(True)
print(myFrinds) # ['walid', 'Mohammed', 'Farag', 'Alaa', 100, True]

myFrinds.append(myOldFrids)
print(myFrinds) # ['walid', 'Mohammed', 'Farag', 'Alaa', 100, True, ['medhat', 'Khalid', 'Ahmed']]
print(myFrinds[2]) # Farag
print(myFrinds[5]) # True
print(myFrinds[6]) # ['medhat', 'Khalid', 'Ahmed'] as one element
print(myFrinds[6][2]) # Ahmed

# extend()  لما اكون عايزهم كلهم يبقو لسته واحده

a = [1, 2, 3]
b = ["a", "b", "d"]

a.extend(b)
print(a)   # [1, 2, 3, 'a', 'b', 'd']

# remove() بتشيل اليمنت معين من اللست

x = [1, 2, 3, "walid", True, "osama"]
x.remove("walid")
print(x)   # [1, 2, 3, True, 'osama']

# sort() بترتب الارقام او الاسترينج ومينفعش اللتنين مع بعض

y = [1, 2, 100, 120, -10, 17, 29]
#y.sort() # = y.sort(reverse=False)
#print(y)  # [-10, 1, 2, 17, 29, 100, 120]

y.sort(reverse=True)
print(y) # [120, 100, 29, 17, 2, 1, -10]

# reverse() 

z = [10, 1, 9, 80, 100, "Walid", 100]
z.reverse()
print(z)   # [120, 100, 29, 17, 2, 1, -10]






