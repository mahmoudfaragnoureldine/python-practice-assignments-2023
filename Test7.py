# ------------------------------
# -- Variables -- =>بيحدد مكان معين فى الميمورى وبيحط فيها الداتا وهو مجرد سيريال
#                    بيعبر عن اسم المكان اللي خزن فيه الداتا فى الميمورى
# -------------------
# syntax => [Variable Name] [Assignment Operatpr] [Value]
# example 
myVariable = "myValue"
print(myVariable)

# Name Convention and Rules
# [1] Can start with (a-z or A-Z) or Underscore (_)
# [2] You cannot start with number or special characters (-)
# [3] Can include numbers (0-9) or underscore
# [3] Cannot include special characters 
# [4] Name is not like name ( Case Sensitive )

name = "Walid Farag"    # single word => Normal
myName = "Walid Farag"  # Two Words => camelCase
my_Name = "Walid Farag" # Two Words => snake_case

print(name)
print(myName)
print(my_Name)