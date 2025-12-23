# ---------------------------------
# -- String Formating (old ways) --
# ---------------------------------

name = "walid"
age = 36 
rank = 10

print("my name is:" + name)
#print("my name is:" + name + " and my age is:" + age)

print("my name is: %s" % "walid") # place holder
print("my name is: %s" % name) 
print("my name is: %s and my age is: %d" % (name, age) )
print("my name is: %s and my age is: %d and my rank is: %f" % (name, age, rank) )

# %s => String
# %d => Number 
# %f => Float
 
n = "walid"
i = "python"
y = 10
print("my name is %s Iam %s developer with %d years exp" % (n, i, y))

# التحكم فى الفلوتينج بوينت
# control floating point number 

myNumber  = 10
print("my number is: %d" % myNumber)
print("my number is: %f" % myNumber) # 10.000000
print("my number is: %.1f" % myNumber) # 10.0
print("my number is: %.2f" % myNumber) # 10.00

# Truncate String

myLongString = "hello people i hate you all"
print("message is: %s" % myLongString)
print("message is: %.5s" % myLongString)
