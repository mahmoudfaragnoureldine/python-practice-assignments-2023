# -----------------------------
# -- String Methods Part Two --
# -----------------------------

# split() rsplit() بتاخد كل العناصر بتاعتك وبتقسمها ل ليست نوع من الداتا تايب
# هى بترجعها عن طريق اللسبيس
a = "i love python and php" # by default
b = "ilovrpythonandphp"
c = "I-love-python-and-php" # by separator
d = "i-love-python-and-php" # by max.split
print(a.split())
print(b.split())
print(c.split("-"))
print(d.split("-", 2))

e = "i-love-python-and-php"
print(d.rsplit("-", 2))

# center()
r = "osama" 
print(r.center(9)) # spaces
print(r.center(9 ,"#"))

# count() ولازم تكزن كابيتال او سومال
#  اعملى كونت لكلكه معينه وشوفها موجوده كم مره

f = "i love python and php because php is easy"
print(f.count("php"))
print(f.count("php" ,0 , 25))

# swapcase() لو الجمله فيها حروف سمال هيحولها لكابيتال والعكس

g = 'i love python'
h = 'i love cpp'
print(g.swapcase())
print(h.swapcase())

# startswich() بتحتاج منك 3 حاجات
# هل الجمله بتاعتك بتبدا بالحرف دا ولا لا 

i = 'i love python'
print(i.startswith("i"))
print(i.startswith("p"))

print(i.startswith("p" ,7 ,12))

# endswith نفس الللى قبلها

o = "i love python"
print(o.endswith("n"))


