# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------

uName  = input('What\'s your name?').strip().capitalize()
uCountry = input('What\'s your country').strip()
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt":
    print(f'Hello {uName} because you are from {uCountry}')
    print(f"The course \"{cName}\" price is ${cPrice - 40}" )

elif uCountry == "KSA":
    print(f'Hello {uName} because you are from {uCountry}')
    print(f"The course \"{cName}\" price is ${cPrice - 50}" )

elif uCountry == "K":
    print(f'Hello {uName} because you are from {uCountry}')
    print(f"The course \"{cName}\" price is ${cPrice - 40}" )

else :
    print(f'Hello {uName} because you are from {uCountry}')
    print(f"The course \"{cName}\" price is ${cPrice - 20}" )
