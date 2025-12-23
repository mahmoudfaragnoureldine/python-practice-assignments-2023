# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess  --
# ----------------------------

print("#" * 50)
print("#" * 50)

tries = 4

mainPass = "Walid120130"

inputPass = input("Please write your password: ")

while inputPass != mainPass:
    tries -= 1
    print(f"Your Password is wrong, { 'Last' if tries == 0 else tries } chance lift")
    inputPass = input("Please write your password: ")

    if tries == 0:
        print("All tries is finished")
        break

else:
    print("Correct Password")
