# --------------------
# -- String Methods --
# --------------------

# len()  it is a buld in function 
      # بترجعلك عن الايتيمز الموجوده فى كونتينر معين 
a = 'I love python'
b = '   I love python   '
print(len(a))
print(len(b))

# strip() rstrip() lstrip()
print(b.strip())
print(b.rstrip())
print(b.lstrip())
print(len(b.strip()))

# note
c = '###I love python###'
print(c.strip("#"))
print(c.rstrip("#"))
print(c.lstrip("#"))

# title()
# بيحول اللسترينج اللى انت بتدهوله لتايتل 
#  فبيخلى اول حرف من كل كلمه كابيتال وبيخلى الحروف اللى بعد الارقام كابيتال
d = "i love 2d graphics 3g technology and python"
print(d.title())

# capitalize() اول حرف من كل كلمه بيبقي كابيتال
e = "i love 2d graphics 3g technology and python"
print(e.capitalize())

# zfill 
f ,g ,h , j = "1" ,"11" ,"111" ,"1111"
print(f)
print(g)
print(h)
print(j)

print(f.zfill(4))
print(g.zfill(4))
print(h.zfill(4))
print(j.zfill(4))

# upper()
k = "walid"
print(k.upper())

# lower()
print(k.lower())

