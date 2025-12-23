# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------

print("#" * 80)
print(" Practice Code: Admin delete or update .".center(80, "#"))
print("#" * 80)

# List contains Admin
admin = ["Walid", "Mahmoud", "Khalid", "Mohammed", "Ashraf"]

# Login
name = input("Please type your name: ").strip().capitalize()

# If name is in admin
if name in admin:
    print("Hello {:s} welcome back".format(name))
    option = input("Delete or Update your name? ").strip().capitalize()

    # Update option
    if option == "Update" or option == "U":
        theNewName = input("Please write your new name: ").strip().capitalize()
        admin[admin.index(name)] = theNewName
        print("name updated")
        print(admin)
    # Delete option
    elif option == "Delete" or option == "D":
        admin.remove(name)
        print("Name Deleted")
        print(admin)
    # Wrong option
    else:
        print("Wrong option")

else:
    status = input("You are not admin, add you: Y or N? ").strip().capitalize()
    # Yes option
    if status == "Yes" or status == "Y":
        admin.append(name)
        print("You are Admin now")
        print(admin)
    # No option
    else:
        print("You are not added")
