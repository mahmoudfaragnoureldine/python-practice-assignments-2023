# --------------------------
# -- Comparison Operators --
# --------------------------
# [ == ] Equal
# [ != ] Not Equal
# [ > ] Greater than
# [ < ] Less than
# [ >= ] Greater than or Equal
# [ <= ] Less than or Equal 
# ----------------------------

# Equal + Not Equal 

print(100 == 100)    # True
print(100 == 200)    # False
print(100 == 100.00) # True

print('#' *45)

print(100 != 100)    # False
print(100 != 200)    # True
print(100 != 100.00) # False

print('#' *45)

# Greater than + Less than

print(100 > 100)    # False
print(100 > 200)    # False
print(100 > 100.00) # False

print('#' *45)

print(100 < 100)    # False
print(100 < 200)    # True
print(100 < 100.00) # False

print('#' *45)

# Greater than or Equal + Less than or Equal

print(100 >= 100)    # True
print(100 >= 200)    # False
print(100 >= 100.00) # True

print('#' *45)

print(100 <= 100)    # True
print(100 <= 200)    # True
print(100 <= 100.00) # True

print('#' *45)