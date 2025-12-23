# -----------------------------
# -- Loop => While Training --
# ----------------------------
# While condition_is_true
# code will run until condition become false
# -------------------------------------------

myF = ["ma", "mo", "wa", "as", "e", "r", "t", "y", "u", "i"]

print(len(myF))  # List length

a = 0

while a < len(myF):
    print(f"#{str(a + 1).zfill(2)} {myF[a]}")
    a += 1

else:
    print("All friends printed to screen")
# print(myF[0])
# print(myF[1])
# print(myF[2])
# print(myF[3])
# print(myF[4])
# print(myF[5])
# print(myF[6])
# print(myF[7])
# print(myF[8])
# print(myF[9])
