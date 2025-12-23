# -----------------
# -- Loop => For --
# -----------------
# for item in iterable_ibject :
#    Do something with item
# -----------------------------

myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in myNumbers:
    # print(number * 17)

    if number % 2 == 0:  # even
        print(f"The Number {number} is Even")

    else:
        print(f"The Number {number} is Odd")

else:
    print("Loop is finished")

myName = "Walid"

for letter in myName:
    print(f"[ {letter.upper()} ]")
