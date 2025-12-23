# --------------------
# -- String Methods --
# --------------------

# index(text ,start ,end) text = Substring اجبارى

a = "i love python"
print(a.index("p")) # index number 7
print(a.index("p" ,0 ,10))
#print(a.index("p" ,0 ,5)) # through error

# find(text ,start ,end) text = Substring اجبارى

a = "i love python"
print(a.find("p")) # index number 7
print(a.find("p" ,0 ,10))
print(a.find("p" ,0 ,5)) # -1

# rjust(width, fill char) ljust(width, fill char)

c = "osama"
print(c.rjust(10))
print(c.rjust(10, "#")) # #####osama

print(c.ljust(10))
print(c.ljust(10, "#")) # osama#####

# splitline() بترجعلك كل اللينز بتاعتك فى ليست

e = """ first kine
second line
third line """
print(type(e.splitlines()))

# expandstabs() بتتحكم فى عدد اللسبيس ما بين التابس 

g = "hello\tworld\ti\tlove\tpython"
print(g.expandtabs(2))

one = "I Iove Python And 3G"
two = "i love python and 3g"
print(one.istitle())
print(two.istitle())

three = " "
print(three.isspace())

four = "i love python"
five = "i love python"
print(four.islower())
print(five.islower())

six = "walid_farag"
seven = "walidFarag"
eight = "walid--farag"

print(six.isidentifier())
print(seven.isidentifier())
print(eight.isidentifier())

x = "AaaaaBbbbb"
y = "AaaaaBbbbb111"
print(x.isalpha()) # from a to z
print(y.isalpha())




