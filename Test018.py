# ---------------------------------
# -- String Formating (new ways) --
# ---------------------------------

name = "walid"
age = 36 
rank = 10

print("my name is:" + name)
#print("my name is:" + name + " and my age is:" + age)

print("my name is: {}".format("walid")) # place holder
print("my name is: {}".format(name))  
print("my name is: {} and my age is: {}" .format(name, age) )
print("my name is: {:s} and my age is: {:d} and my rank is: {:f}".format(name, age, rank) )

# {:s} => String
# {:d} => Number 
# {:f} => Float
 
n = "walid"
i = "python"
y = 10
print("my name is {:s} Iam {:s} developer with {:d} years exp".format(n, i, y))

# التحكم فى الفلوتينج بوينت
# control floating point number 

myNumber  = 10
print("my number is: {:d}".format(myNumber))
print("my number is: {:f}" .format(myNumber)) # 10.000000
print("my number is: {:.1f}".format(myNumber)) # 10.0
print("my number is: {:.2f}".format(myNumber)) # 10.00

# Truncate String

myLongString = "hello people i hate you all"
print("message is: {}".format(myLongString))
print("message is: {:.5s}".format(myLongString))

# Format Money

myMoney = 500122658987411
print("my money is bank is: {:d}".format(myMoney))
print("my money is bank is: {:_d}".format(myMoney))
print("my money is bank is: {:,d}".format(myMoney))
#print("my money is bank is: {:&d}".format(myMoney)) # wrong

# ReArrange Items 

a, b, c = "One", "two", "three"
print("hello {} {} {}".format(a, b, c)) # hello One two three
print("hello {1} {2} {0}".format(a, b, c)) # hello two three one

x, y, z = 10, 20, 30
print("hello {} {} {}".format(x, y, z)) 
print("hello {1:d} {2:d} {0:d}".format(x, y, z))
print("hello {1:f} {0:f} {2:f}".format(x, y, z)) 
print("hello {1:.2f} {2:.3f} {0:.1f}".format(x, y, z))

# Format in Version 3.6+ 

myName = "walid"
myAge = 36
print("my name is: {myName} and my age is: {myAge}")
print(f"my name is: {myName} and my age is: {myAge}")

