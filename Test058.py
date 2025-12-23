# -------------------------------------------------
# -- Function Packing, Unpacking Arguments *Args --
# -------------------------------------------------

# print(1, 2, 3, 4)

# myList = [1, 2, 3, 4]

# print(myList)  # [1, 2, 3, 4]
# print(*myList)  # 1 2 3 4


# def say_hello(*people):  # عشتن يكون فيها اى عدد من الارجيومنت حتى لو انا مش عارفه
#  for name in people:
#       print(f"Hello {name}")


# say_hello("Walid", "Ahmed", "Sayed", "Shraf", "AS")


def show_deteile(name, *skills):
    print(f"Hello {name} your Skills is: ")
    for skill in skills:
        print(skill)


show_deteile("Walid", "Python", "PLC", "Cpp")
