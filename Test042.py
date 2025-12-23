# ---------------
# -- Nested If --
# ---------------

uName  = "Walid"
isStudent = "Yes"
uCountry = "KSA"
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar" :
    
    if isStudent == "Yes" :
        print(f'Hello {uName} because you are from {uCountry} and Student')
        print(f"The course \"{cName}\" price is ${cPrice - 90}" )

    else :
        print(f'Hello {uName} because you are from {uCountry}')
        print(f"The course \"{cName}\" price is ${cPrice - 80}" )

elif uCountry == "Kuwait" or uCountry == "Bahrain" :
    print(f'Hello {uName} because you are from {uCountry}')
    print(f"The course \"{cName}\" price is ${cPrice - 40}" )

else :
    print(f'Hello {uName} because you are from {uCountry}')
    print(f"The course \"{cName}\" price is ${cPrice - 20}" )

