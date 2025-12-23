# ----------------
# -- User Input --
# ----------------

fName = input("What's youe first name?")
mName = input("What's your middle name?")
lName = input('What\'s your last name?')

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

print(f"Hello {fName} {mName:.1s} {lName} nice to see you.")
