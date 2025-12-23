# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in
# --------------------------

# عندك ليست فيها مجموعه عناصر وعايز تساله العنصر دا عضو فى المجموعه دى ولا لا

# String

name = "walid"
print("w" in name)  # true
print("f" in name)  # false

print("#" * 30)

# List

friends = ["Ahmed", "Sayed", "Mahmoud"]
print("Osama" in friends)  # False
print("Mahmoud" in friends)  # Treue
print("Sayad" not in friends)  # True

print("#" * 30)

# Using In and Not In with Condition

countries1 = ["Egypt", "KSA", "Kuwait", "Bahrain"]
countries1Discount = 80

countries2 = ["Italy", "USA"]
countries2Discount = 50

myCountry = "roma"

if myCountry in countries1:
    print(f"Hello you have a discount equal to ${countries1Discount}")

elif myCountry in countries2:
    print(f"Hello you have a discount equal to ${countries2Discount}")

else:
    print("Your country is not in the list")
