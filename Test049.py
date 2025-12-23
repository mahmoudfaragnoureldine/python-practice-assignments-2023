# ----------------------------
# -- Loop => While Training --
# -- Simple Bookmark Manage --
# ----------------------------

# Empty list to fill later
myFavouritWebs = []

# Maximum Allowed Websites
maximumWebs = 5

while maximumWebs > 0:
    # Input the new website
    web = input("Website name without http:// ")

    # Add the new website to the list
    myFavouritWebs.append(f"https://{web.strip().lower()}")

    # Decrease one Number from allowed website
    maximumWebs -= 1

    # Print the add message
    print(f"Website added, {maximumWebs} Places lift")

    # Print the list
    print(myFavouritWebs)

else:
    print("Bookmark is full you cant add more")

# Check if list is not empty
if len(myFavouritWebs) > 0:
    # Sort the list
    myFavouritWebs.sort()

    index = 0

    print("Printing The List Websites in Your Bookmarks")

    while index < len(myFavouritWebs):
        print(myFavouritWebs[index])

        index += 1
