# -------------------------
# String Indexing & Slicing
# [1] All data on Python is Object
# [2] Object contains elements
# [3] Every element has its own Index => الايندكس هو الرقم اللي عن طريقه نقدر نوصل للعنصر دا
# [4] Python use zero Based indexing ( Index start from zero )
# [5] Use square brackets to access element
# [6] Enable Accessing parts of string, tuples or lists
# -----------------------------------------------------

# Indexing ( access single item )

myString = "I love python"

print(myString[0]) # index 0 => I 
print(myString[9]) # index 9 => t

print(myString[-1]) # index -1 => first character from end
print(myString[-6]) # index -6 => 6th character from end

# Slicing ( Access Multiple Sequance Items )
# [Start:End] End not included
# [Start:End:Steps]

print(myString[8:11]) # yth
print(myString[3:5])  # ov

print(myString[:10]) # if start is not here will start from 0 (I love pyt)
print(myString[5:]) # if end is not here will go to the end
print(myString[:]) # Full Data

print(myString[0::1]) # Full Data
print(myString[::1]) # Full Data

print(myString[::2])
print(myString[::3])

 
